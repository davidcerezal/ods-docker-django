from django.core.management.base import BaseCommand, CommandError

from odds.domain.models.manager.betTypeManager import BetTypeManager
from odds.domain.models.bet import Bet
from odds.domain.models.sureBet import SureBet
from odds.domain.models.manager.SureBetManager import SureBetManager
from odds.domain.models.event import Event


class Command(BaseCommand):
    SUREBET_PERCENTAGE = 0.99

    def handle(self, *args, **options):
        inserts = 0

        self.surebets_manager = SureBetManager()
        self.betTypeManager = BetTypeManager()
        events = Event.objects.all()
        bets = Bet.objects.all()
        bets.update(revised=False)
        try:
            for event in events:
                if len(event.bets.filter(revised=False)) > 0:
                    self.stdout.write(self.style.SUCCESS('Reviewing "%s"' % event.name))
                    surebet_created = self.calculate_surebets(event, event.bets.all())
                    inserts += 1 if surebet_created else 0
                    if surebet_created:
                        self.stdout.write(self.style.SUCCESS('Surebet inserted on "%s"' % event.name))

        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Request failed %s' % e))

        self.stdout.write(self.style.SUCCESS('inserted "%s"' % inserts))

    def calculate_surebets(self, event, event_bets):
        surebets_created = 0
        surebets_created += self.calculate_surebets_by_key(event, event_bets, 'Match Winner')

        surebets_created += self.calculate_surebets_by_key(event, event_bets, 'Second Half Winner')

        surebets_created += self.calculate_surebets_by_key(event, event_bets, 'Goals Over/Under')

        for bet in event_bets:
            bet.revised = True
            bet.save()

        return surebets_created

    def calculate_surebets_by_key(self, event, event_bets, general_ods_type_key):
        surebet_createds = 0

        checked_types = dict()
        if self.betTypeManager.get_basic_bets()[general_ods_type_key]:
            for ods_type, type in self.betTypeManager.get_basic_bets()[general_ods_type_key].items():

                if ods_type in checked_types:
                    continue

                check_items, checked_types = self.init_to_check_items(checked_types, ods_type, type)

                check_items = self.find_best_prices(check_items, event_bets)

                all_bets_exists = True
                for key, ods_type in check_items.items():
                    if ods_type['bet'] == 0:
                        all_bets_exists = False

                if all_bets_exists:
                    ratio = 0
                    all_bets = dict()
                    minimum_types_ratio = dict()
                    for key, ods_type in check_items.items():
                        ratio += 1 / ods_type['best_ratio']
                        minimum_types_ratio[key] = ods_type['best_ratio']

                    if ratio < self.SUREBET_PERCENTAGE:
                        all_bets = self.find_and_add_other_possible_bets(all_bets, event_bets, minimum_types_ratio)

                        self.surebets_manager.create(ods_type[0]['bet'].name.name, 1 / ratio, all_bets, event, True)
                        surebet_createds += 1

        return surebet_createds

    def find_and_add_other_possible_bets(self, all_bets, event_bets, minimum_types_ratio):
        for ods_type, bet_check_ratio in minimum_types_ratio.items():
            values_ratio_to_less = self.SUREBET_PERCENTAGE
            for ods_type_other, bet_check_ratio in minimum_types_ratio.items():
                if ods_type_other != ods_type:
                    values_ratio_to_less -= (1 / bet_check_ratio)

            minimun_ratio = 1 / values_ratio_to_less

            for bet in event_bets:
                if len(bet.market.all()) > 0 and bet.type.all()[0].identifier == ods_type and bet.price > minimun_ratio:
                    all_bets[bet.id] = bet

        return all_bets

    def find_best_prices(self, check_items, event_bets):
        for key, ods_type in check_items.items():
            for bet in event_bets:
                if len(bet.market.all()) > 0:
                    if bet.type.all()[0].identifier == ods_type['type'] and bet.price > ods_type['best_ratio']:
                        ods_type['bet'] = bet
                        ods_type['best_ratio'] = bet.price

        return check_items

    def init_to_check_items(self, checked_types, ods_type, type):
        check_items = dict()
        # CURRENT TYPE
        checked_types[ods_type] = ods_type
        check_items[ods_type] = {
            'type': ods_type,
            'bet': 0,
            'best_ratio': 0
        }
        # OPPOSITE TYPES
        for opposite_ods_type in type['opposite'] if isinstance(type['opposite'], list) else [type['opposite']]:
            checked_types[opposite_ods_type] = opposite_ods_type
            check_items[opposite_ods_type] = {
                'type': opposite_ods_type,
                'bet': 0,
                'best_ratio': 0
            }

        return check_items, checked_types

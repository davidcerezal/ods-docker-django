from django.core.management.base import BaseCommand, CommandError

from odds.domain.models.bet import Bet
from odds.domain.models.sureBet import SureBet
from odds.domain.models.manager.SureBetManager import SureBetManager
from odds.domain.models.event import Event


class Command(BaseCommand):
    def handle(self, *args, **options):
        inserts = 0

        try:
            for surebet in SureBet.objects.filter(revised=False).all():
                self.revise_surebets(surebet)

        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Request failed %s' % e))

        self.stdout.write(self.style.SUCCESS('inserted "%s"' % inserts))

    def revise_surebets(self, event):
        return self.calculate_win_loss_surebets(event)

    def calculate_win_loss_surebets(self, event, event_bets):
        surebet_created = False
        best_ratio_win = best_ratio_tie = best_ratio_loss = 0
        bet_win = bet_tie = bet_loss = 0
        for bet in event_bets:
            if len(bet.market.all()) > 0:
                if bet.type.all()[0].identifier == 'H1' and bet.price > best_ratio_win:
                    best_ratio_win = bet.price
                    bet_win = bet
                elif bet.type.all()[0].identifier == 'TX' and bet.price > best_ratio_tie:
                    best_ratio_tie = bet.price
                    bet_tie = bet
                elif bet.type.all()[0].identifier == 'A2' and bet.price > best_ratio_loss:
                    best_ratio_loss = bet.price
                    bet_loss = bet

        if bet_win != 0 and bet_tie != 0 and bet_loss != 0:
            ratio = (1 / best_ratio_win) + (1 / best_ratio_tie) + (1 / best_ratio_loss)
            if ratio < 1:
                self.surebets_manager.create(bet_win.name, 1 / ratio, {bet_win, bet_tie, bet_loss}, event, True)
                surebet_created = True
                for bet in event_bets:
                    bet.revised = True
                    bet.save()

        return surebet_created
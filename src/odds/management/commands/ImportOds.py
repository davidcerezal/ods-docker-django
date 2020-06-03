from django.core.management.base import BaseCommand, CommandError
from odds.domain.models.bet import Bet
from odds.domain.models.event import Event
from odds.domain.models.sureBet import SureBet
from odds.domain.models.betMarket import BetMarket
from odds.domain.services.provider.footballDataExtractor import FootBallDataExtractor
from odds.domain.models.manager.betTypeManager import BetTypeManager
from odds.domain.models.sureBet import SureBet


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('import_page_name', nargs='+', type=str)

    def handle(self, *args, **options):
        inserts = 0
        football_data_extractor = FootBallDataExtractor()
        bet_type_manager = BetTypeManager()

        try:
            bet_type_manager.init_basic_bet_type()
            football_data_extractor.request()
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Request failed %s' % e))

        self.stdout.write(self.style.SUCCESS('inserted "%s"' % inserts))

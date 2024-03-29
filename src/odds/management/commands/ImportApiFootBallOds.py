from django.core.management.base import BaseCommand, CommandError
from odds.domain.services.provider.ApiFootBallExtractor import ApiFootBallDataExtractor
from odds.domain.models.manager.betTypeManager import BetTypeManager


class Command(BaseCommand):
    def handle(self, *args, **options):
        inserts = 0
        api_football_data_extractor = ApiFootBallDataExtractor()
        bet_type_manager = BetTypeManager()

        try:
            bet_type_manager.init_basic_bet_type()
            self.stdout.write(self.style.SUCCESS('Requesting odds'))
            inserts += api_football_data_extractor.do_request()
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Request failed %s' % e))

        self.stdout.write(self.style.SUCCESS('inserted "%s"' % inserts))

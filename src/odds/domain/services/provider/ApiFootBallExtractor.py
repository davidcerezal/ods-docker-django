from odds.domain.services.provider.request.ApiFootballServiceRequest import ApiFootballServiceRequest
from odds.domain.services.provider.parser.apiFootball import ApiFootBallDataParser


class ApiFootBallDataExtractor:

    leagues = {
        'España 1º': 775,
        'Alemania 1º': 754,
        'España 2º': 775,
        'Alemania 2º': 755
    }

    def __init__(self):
        self.request = ApiFootballServiceRequest()
        self.parser = ApiFootBallDataParser()

    def do_request(self):
        # Get next fixture
        for league, league_item in self.leagues.items():
            fixtures = self.request.call_next_fixtures_by_league(league_item)
            if not fixtures:
                continue

            fixtures = self.parser.parse_next_fixtures_response(fixtures)
            if len(fixtures) <= 0:
                continue

            self.__create_odds(fixtures)

    def __create_odds(self, fixtures):
        for fixture, event in fixtures.items():
            odds = self.request.call_get_odds_by_fixture(fixture)
            if not odds:
                continue

            fixtures = self.parser.create_ods(odds, event)



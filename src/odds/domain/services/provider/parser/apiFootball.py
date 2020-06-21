from odds.domain.models.manager.betTypeManager import BetTypeManager
from odds.domain.models.betType import BetType
from odds.domain.models.betMarket import BetMarket
from odds.domain.models.manager.EventManager import EventManager
from odds.domain.models.manager.betManager import BetManager
from odds.domain.models.manager.betMarketManager import BetMarketManager
from pytz import timezone
import datetime
import pytz


class ApiFootBallDataParser:
    allowed_ods = ['Match Winner', 'Second Half Winner', 'Goals Over/Under']

    def __init__(self):
        self.betMarketManager = BetMarketManager()
        self.betManager = BetManager()
        self.event_manager = EventManager()
        self.BetTypeManager = BetTypeManager()

    def parse_next_fixtures_response(self, lines_fixtures):
        fixtures_ids = dict()
        for fixture in lines_fixtures:
            date = datetime.datetime.strptime(fixture.get('event_date')[:-6], '%Y-%m-%dT%H:%M:%S')
            date = pytz.utc.localize(date)
            event = self.event_manager.create_or_find_event(
                fixture.get('homeTeam').get('team_name'),
                fixture.get('awayTeam').get('team_name'),
                date)
            if event:
                fixtures_ids[str(fixture.get('fixture_id'))] = event
        return fixtures_ids

    def create_ods(self, odds, event):
        for bookmaker in odds.get('bookmakers'):
            if len(BetMarket.objects.filter(name=bookmaker.get('bookmaker_name'))) <= 0:
                self.create_bet_market(bookmaker.get('bookmaker_name'))

            for bet in bookmaker.get('bets'):
                if bet.get('label_name') in self.allowed_ods:
                    for value in bet.get('values'):
                        if self.find_winner_type(bet.get('label_name'), value.get('value')) == False:
                            continue

                        bet_created = self.betManager.create_bet(
                            event.name,
                            value.get('odd'),
                            event.date,
                            BetMarket.objects.filter(name=bookmaker.get('bookmaker_name'))[0],
                            self.find_winner_type(bet.get('label_name'), value.get('value')), False)
                        event.bets.add(bet_created)
                        event.save()

    def create_bet_market(self, bookmaker):
        bet_market = self.betMarketManager.create_bet_market(bookmaker)
        bet_market.save()

    def find_winner_type(self, ods_type, key):
        finder = ''
        if ods_type in self.BetTypeManager.get_basic_bets():
            finder = self.BetTypeManager.get_bet_mapped(ods_type, key, 'apiFootballKey')

        if not finder or finder == '':
            return False

        # if ods_type == 'Match Winner':
        #     if key == 'Home':
        #         finder = 'H1'
        #     elif key == 'Draw':
        #         finder = 'TX'
        #     elif key == 'Away':
        #         finder = 'A2'
        #     else:
        #         raise Exception('Type Not Found')
        #
        # elif ods_type == 'Second Half Winner':
        #     if key == 'Home':
        #         finder = '2partH1'
        #     elif key == 'Draw':
        #         finder = '2partTX'
        #     elif key == 'Away':
        #         finder = '2partA2'
        #     else:
        #         raise Exception('Type Not Found')
        #
        # elif ods_type == 'Goals Over/Under':
        #     if key == 'Over 3.5':
        #         finder = '03.5'
        #     elif key == 'Under 3.5':
        #         finder = 'U3.5'
        #     elif key == 'Over 1.5':
        #         finder = '01.5'
        #     elif key == 'Under 1.5':
        #         finder = 'U1.5'
        #     elif key == 'Over 4.5':
        #         finder = '04.5'
        #     elif key == 'Under .5':
        #         finder = 'U4.5'
        #     elif key == 'Over 5.5':
        #         finder = '05.5'
        #     elif key == 'Under 0.5':
        #         finder = 'U0.5'
        #     elif key == 'Over 2.5':
        #         finder = '02.5'
        #     elif key == 'Under 2.5':
        #         finder = 'U2.5'
        #     else:
        #         raise Exception('Type Not Found')

        if finder == '' or len(BetType.objects.filter(identifier=finder)) <= 0:
            return False

        return BetType.objects.filter(identifier=finder)[0]

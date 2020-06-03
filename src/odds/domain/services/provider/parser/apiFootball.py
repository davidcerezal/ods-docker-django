from odds.domain.models.betType import BetType
from odds.domain.models.betMarket import BetMarket
from odds.domain.models.manager.EventManager import EventManager
from odds.domain.models.manager.betManager import BetManager
from odds.domain.models.manager.betMarketManager import BetMarketManager
from pytz import timezone
import datetime



class ApiFootBallDataParser:
    allowed_ods = ['Match Winner']

    def __init__(self):
        self.betMarketManager = BetMarketManager()
        self.betManager = BetManager()
        self.event_manager = EventManager()


    def parse_next_fixtures_response(self, lines_fixtures):
        fixtures_ids = dict()
        for fixture in lines_fixtures:
            date = datetime.datetime.strptime(fixture.get('event_date')[:-6], '%Y-%m-%dT%H:%M:%S')
            date.replace(tzinfo=timezone('UTC'))
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
                        bet = self.betManager.create_bet(
                            event.name,
                            value.get('odd'),
                            event.date,
                            BetMarket.objects.filter(name=bookmaker.get('bookmaker_name'))[0],
                            self.find_winner_type(value.get('value')), False)
                        event.bets.add(bet)
                        event.save()

    def create_bet_market(self, bookmaker):
        bet_market = self.betMarketManager.create_bet_market(bookmaker)
        bet_market.save()

    def find_winner_type(self, key):
        if key == 'Home':
            return BetType.objects.filter(identifier='H1')[0]
        elif key == 'Draw':
            return BetType.objects.filter(identifier='TX')[0]
        elif key == 'Away':
            return BetType.objects.filter(identifier='A2')[0]
        else:
            raise Exception('Type Not Found')


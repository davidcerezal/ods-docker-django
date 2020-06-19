from django.db import models
from odds.domain.models.betType import BetType
from odds.domain.models.factories.betType import BetTypeFactory


class BetTypeManager:

    basic_bet = {
        'Match Winner': {
            'H1': {
                'desc': 'Home winner',
                'value': '1',
                'opposite': ['TX', 'A2'],
                'apiFootballKey': 'Home'
            },
            'TX': {
                'desc': 'Tie match',
                'value': 'X',
                'opposite': ['H1', 'A2'],
                'apiFootballKey': 'Draw'
            },
            'A2': {
                'desc': 'Away winner',
                'value': '2',
                'opposite': ['TX', 'H1'],
                'apiFootballKey': 'Away'
            }
        },
        'Second Half Winner': {
            '2partH1': {
                'desc': 'Second Part Home winner',
                'value': '1',
                'opposite': ['2partTX', '2partA2'],
                'apiFootballKey': 'Home'
            },
            '2partTX': {
                'desc': 'Second Part Tie match',
                'value': 'X',
                'opposite': ['2partA2', '2partH1'],
                'apiFootballKey': 'Draw'
            },
            '2partA2': {
                'desc': 'Second Part Away winner',
                'value': '2',
                'opposite': ['2partTX', '2partH1'],
                'apiFootballKey': 'Away'
            },
        },
        'Goals Over/Under': {
            'O1.5': {
                'desc': 'Goals Over 1.5',
                'value': '1',
                'opposite': 'U1.5',
                'apiFootballKey': 'Over 1.5'
            },
            'U1.5': {
                'desc': 'Goals Under 1.5',
                'value': '2',
                'opposite': 'O1.5',
                'apiFootballKey': 'Under 1.5'
            },
            'O4.5': {
                'desc': 'Goals Over 4.5',
                'value': '1',
                'opposite': 'U4.5',
                'apiFootballKey': 'Over 4.5'
            },
            'U4.5': {
                'desc': 'Goals Under 3.5',
                'value': '2',
                'opposite': 'O4.5',
                'apiFootballKey': 'Under 4.5'
            },
            'O2.5': {
                'desc': 'Goals Over 2.5',
                'value': '1',
                'opposite': 'U2.5',
                'apiFootballKey': 'Over 2.5'
            },
            'U2.5': {
                'desc': 'Goals Under 2.5',
                'value': '2',
                'opposite': 'O2.5',
                'apiFootballKey': 'Under 2.5'
            },
            'O0.5': {
                'desc': 'Goals Over 0.5',
                'value': '1',
                'opposite': 'U0.5',
                'apiFootballKey': 'Over 0.5'
            },
            'U0.5': {
                'desc': 'Goals Under 0.5',
                'value': '2',
                'opposite': 'O0.5',
                'apiFootballKey': 'Under 0.5'
            },
            'O5.5': {
                'desc': 'Goals Over 5.5',
                'value': '1',
                'opposite': 'U5.5',
                'apiFootballKey': 'Over 5.5'
            },
            'U5.5': {
                'desc': 'Goals Under 5.5',
                'value': '2',
                'opposite': 'O5.5',
                'apiFootballKey': 'Under 5.5'
            },
            'O3.5': {
                'desc': 'Goals Over 3.5',
                'value': '1',
                'opposite': 'U3.5',
                'apiFootballKey': 'Over 3.5'
            },
            'U3.5': {
                'desc': 'Goals Under 3.5',
                'value': '2',
                'opposite': 'O3.5',
                'apiFootballKey': 'Under 3.5'
            }
        }
    }

    def __init__(self):
        self.betTypeFactory = BetTypeFactory()

    def get_basic_bets(self):
        return self.basic_bet

    def get_bet_mapped(self, ods_type, key, data_manager):
        if ods_type in self.get_basic_bets():
            for key, bet_type in self.basic_bet[ods_type].items():
                if bet_type[data_manager] and bet_type[data_manager] == key:
                    return key
        else:
            return False

    def create_bet_type(self, identifier, description, value):
        if len(BetType.objects.filter(identifier=identifier)):
            return self.betTypeFactory.create(identifier, description, value)
        else:
            return BetType.objects.filter(identifier=identifier)[0]

    def init_basic_bet_type(self):
        """
        Creates the basics bets H1, TX, A2
        :return:
        """
        for key, value in self.basic_bet.items():
            if len(BetType.objects.filter(identifier=key)) == 0:
                bet_type = self.betTypeFactory.create(key, value['desc'], value['value'])
                bet_type.save()

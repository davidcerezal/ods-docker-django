from django.db import models
from odds.domain.models.betType import BetType
from odds.domain.models.factories.betType import BetTypeFactory


class BetTypeManager:
    basic_bet = {
        'H1': {
            'desc': 'Home winner',
            'value': '1'
        },
        'TX': {
            'desc': 'Tie match',
            'value': 'X'
        },
        'A2': {
            'desc': 'Away winner',
            'value': '2'
        }
    }

    def __init__(self):
        self.betTypeFactory = BetTypeFactory()

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

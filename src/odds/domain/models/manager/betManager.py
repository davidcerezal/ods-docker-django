from django.db import models
from odds.domain.models.bet import Bet
from odds.domain.models.factories.bet import BetFactory


class BetManager:

    def __init__(self):
        self.betFactory = BetFactory()

    def create_bet(self, name, price, expiry_date, market, type, revised=False):
        # SHOULD CHECK IF THERE IS ANOTHER WITH THE SAME PRICE
        return self.betFactory.create(name, price, expiry_date, market, type, revised)


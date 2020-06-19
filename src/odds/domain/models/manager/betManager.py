from django.db import models

from odds.domain.models.sureBet import SureBet
from odds.domain.models.bet import Bet
from odds.domain.models.factories.bet import BetFactory


class BetManager:

    def __init__(self):
        self.betFactory = BetFactory()

    def create_bet(self, name, price, expiry_date, market, type, revised=False):
        if len(Bet.objects.filter(name=name, expiry_date=expiry_date, market=market, type=type).all()) > 0:
            bet = Bet.objects.filter(name=name, expiry_date=expiry_date, market=market, type=type).all()[0]
            bet.updatePrice(price)
            SureBet.objects.filter(bets__in=[bet]).all().update(revised=False)

        else:
            bet = self.betFactory.create(name, price, expiry_date, market, type, revised)
        return bet


from django.db import models
from odds.domain.models.betMarket import BetMarket
from odds.domain.models.factories.betMarket import BetMarketFactory


class BetMarketManager:

    def __init__(self):
        self.betMarketFactory = BetMarketFactory()

    def create_bet_market(self, title):
        if (len(BetMarket.objects.filter(name=title)) == 0 and
                 len(BetMarket.objects.filter(alias__contains=title)) == 0
        ):
            return self.betMarketFactory.create(title)
        else:
            return BetMarket.objects.filter(name=title)[0]


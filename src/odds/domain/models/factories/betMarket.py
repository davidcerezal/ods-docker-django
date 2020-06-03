from odds.infrastructure.persistence.bet_repository import BetRepository
from odds.domain.models.betMarket import BetMarket


class BetMarketFactory(object):

    @classmethod
    def create(cls, title):
        return BetMarket(name=title, alias=title, url=title)

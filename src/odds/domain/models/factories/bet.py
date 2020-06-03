from odds.infrastructure.persistence.bet_repository import BetRepository
from odds.domain.models.bet import Bet


class BetFactory(object):

    @classmethod
    def create(cls, name, price, expiry_date, market, type, revised=False):
        price = float(price)
        if price is None or price < 0:
            raise Exception('Price cannot be negative')

        bet = Bet(name=name, price=price, expiry_date=expiry_date, revised=revised)
        bet.save()

        bet.market.add(market)
        bet.type.add(type)

        return bet

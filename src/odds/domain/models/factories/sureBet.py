from odds.domain.models.sureBet import SureBet
import datetime
import pytz


class SureBetFactory(object):

    @classmethod
    def create(cls, name, benefit, bets, revised=False):
        surebet = SureBet(name=name, benefit=benefit, revised=revised)
        surebet.save()
        for bet in bets:
            surebet.bets.add(bet)

        return surebet

from odds.domain.models.sureBet import SureBet
import datetime
import pytz


class SureBetFactory(object):

    @classmethod
    def create(cls, name, benefit, bets, event, revised=False):
        surebet = SureBet(name=name, benefit=benefit, revised=revised)
        surebet.save()
        surebet.events.add(event)
        for bet in bets:
            surebet.bets.add(bet)

        return surebet

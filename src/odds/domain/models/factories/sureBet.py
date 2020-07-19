from odds.domain.models.sureBet import SureBet
import datetime
import pytz


class SureBetFactory(object):

    @classmethod
    def create(cls, name, benefit, bets, event, revised=False):
        surebet = SureBet(name=name, benefit=benefit, revised=revised, type=SureBet.TYPE_NORMAL)
        surebet.save()
        surebet.events.add(event)
        for bet in bets:
            surebet.bets.add(bet)

        return surebet


    @classmethod
    def createCombined(cls, name, benefit, bets, combinedBets, event, revised=False):
        surebet = SureBetFactory.create(name=name, benefit=benefit, bets=bets, event=event, revised=revised)
        surebet.type = SureBet.TYPE_COMBINED
        for bet in combinedBets:
            surebet.combined_bets_first.add(bet)
        surebet.save()

        return surebet
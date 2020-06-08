from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from odds.domain.models.betType import BetType
from odds.domain.models.sureBet import SureBet
from odds.domain.models.bet import Bet


@login_required(login_url="/login/")
def sureBetDetail(request, surebet_id):
    try:
        surebet = SureBet.objects.get(pk=surebet_id)
    except Bet.DoesNotExist:
        raise Http404("Poll does not exist")

    first_bet = surebet.bets.all()[0]
    event = first_bet.event_set.all()[0]
    types = dict()
    for type in surebet.getTypes():
        types[type.name] = surebet.getBestBetByType(type)

    other_bets = dict()
    for n in range(1, 10):
        other_bets_temp = dict()
        other_bets_temp['H1'] = event.getBestBetByType(BetType.objects.get(identifier='H1'), n)
        other_bets_temp['TX'] = event.getBestBetByType(BetType.objects.get(identifier='TX'), n)
        other_bets_temp['A2'] = event.getBestBetByType(BetType.objects.get(identifier='A2'), n)
        other_bets[n] = other_bets_temp

    return render(request, "bet/bet-detail.html", {
        'surebet': surebet,
        'bet_global_type': surebet.getGloblaType(),
        'types': types,
        'event': event,
        'other_bets': other_bets
    })


class BetList(object):
    pass
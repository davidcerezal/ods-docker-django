from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from odds.domain.models.sureBet import SureBet
from odds.domain.models.event import Event


@login_required(login_url="/login/")
def index(request):
    last_sure_bets = SureBet.objects.all()[:10]

    surebet_set = []
    for surebet in last_sure_bets:
        surebet_temp = dict()
        first_bet = surebet.bets.all()[0]
        event = first_bet.event_set.all()
        surebet_temp['surebet'] = surebet
        surebet_temp['event'] = event[0]
        surebet_temp['types'] = dict()
        surebet_temp['bet_global_type'] = surebet.getGloblaType()
        for type in surebet.getTypes():
            surebet_temp['types'][type.name] = surebet.getBestBetByType(type)

        surebet_set.append(surebet_temp)

    return render(request, "index.html", {
        'surebets': surebet_set
    })

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

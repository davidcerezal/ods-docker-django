from django.views.generic import TemplateView, ListView
from odds.domain.models.bet import Bet


class BetList(ListView):
    template_name = 'bet/bet.html'
    queryset = Bet.objects.all()[:5]

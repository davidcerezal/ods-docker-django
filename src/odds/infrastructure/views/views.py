from django.views.generic import TemplateView, ListView
from odds.domain.tasks.tasks import show_hello_world
from odds.domain.models.bet import BetModel


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BetList(ListView):
    template_name = 'bet/bet.html'
    queryset = BetModel.objects.all()[:5]

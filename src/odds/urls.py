from django.urls import path

from .infrastructure.views.views import BetList

urlpatterns = [
    path('bets/', BetList.as_view(), name='bet-list'),
]

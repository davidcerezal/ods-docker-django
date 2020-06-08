from django.db import models
from odds.domain.models.event import Event
from odds.domain.models.factories.sureBet import SureBetFactory


class SureBetManager:

    def __init__(self):
        self.sureBetFactory = SureBetFactory()

    def create(self, name, benefit, bets, event, revised=False):
        surebet = self.sureBetFactory.create(name, benefit, bets, event, revised)
        return surebet


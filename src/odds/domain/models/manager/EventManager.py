from django.db import models
from odds.domain.models.event import Event
from odds.domain.models.factories.event import EventFactory


class EventManager:


    def __init__(self):
        self.eventFactory = EventFactory()

    def create_or_find_event(self, home_player, away_player2, date, betable=False, description='', name=''):
        if len(Event.objects.filter(player1=home_player, player2=away_player2, date=date)) == 0:
            event = self.eventFactory.create(home_player, away_player2, date, betable, description, name)
            event.save()

            return event
        else:
            return Event.objects.filter(player1=home_player, player2=away_player2, date=date)[0]


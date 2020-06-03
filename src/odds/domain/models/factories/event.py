from odds.domain.models.event import Event
import datetime
import pytz


class EventFactory(object):

    @classmethod
    def create(cls, home_player, away_player2, date, betable=False, description='', name=''):
        name = home_player+'-'+away_player2 if name == '' else name
        return Event(name=name,
                     description=description,
                     player1=home_player,
                     player2=away_player2,
                     date=date,
                     betable=betable,
                     revised=False)

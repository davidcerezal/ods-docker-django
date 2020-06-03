from django.db import models
from odds.domain.services.provider.parser.footballData import FootBallDataParser
from odds.domain.models.manager.EventManager import EventManager
import urllib3



class FootBallDataExtractor:
    url = ''
    url1 = 'http://football-data.co.uk/mmz4281/1920/SP1.csv'

    def __init__(self, url=''):
        self.http = urllib3.PoolManager()
        self.url = self.url1 if url == '' else url
        self.parser = FootBallDataParser()
        self.event_manager = EventManager()

    def request(self):
        df = self.http.request('GET', self.url1)
        lines = "".join(map(chr, df.data)).split('\n')

        self.parser.initialize_markets(lines[0])
        # Hacerlo por bloques
        self.__create_odds(lines[1:])


    def __create_odds(self, lines):
        for line in lines:
            event = self.event_manager.create_or_find_event(
                self.parser.get_player_home(line),
                self.parser.get_player_away(line),
                self.parser.get_date(line), False)

            self.parser.create_ods(event, line)
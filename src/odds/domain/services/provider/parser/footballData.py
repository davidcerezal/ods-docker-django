import datetime
from pytz import timezone
from django.db import models
from django.utils.dateparse import parse_date, parse_datetime
from odds.domain.models.betMarket import BetMarket
from odds.domain.models.betType import BetType
from odds.domain.models.manager.betManager import BetManager
from odds.domain.models.manager.betMarketManager import BetMarketManager



class FootBallDataParser:
    markets = {
        'Bet365': {
            'B365H': 0,
            'B365D': 0,
            'B365A': 0,
        },
        'Blue Square': {
            'BSH': 0,
            'BSD': 0,
            'BSA': 0,
        },
        'Bet&Win': {
            'BWH': 0,
            'BWD': 0,
            'BWA': 0,
        },
        'Gamebookers': {
            'GBH': 0,
            'GBD': 0,
            'GBA': 0,
        },
        'Interwetten': {
            'IWH': 0,
            'IWD': 0,
            'IWA': 0,
        },
        'Ladbrokes': {
            'LBH': 0,
            'LBD': 0,
            'LBA': 0,
        },
        'Pinnacle': {
            'PSH': 0,
            'PSD': 0,
            'PSA': 0,
        },
        'Stan James': {
            'SJH': 0,
            'SJD': 0,
            'SJA': 0,
        },
        'Stanleybet': {
            'SYH': 0,
            'SYD': 0,
            'SYA': 0,
        },
        'VC Bet': {
            'VCH': 0,
            'VCD': 0,
            'VCA': 0,
        },
        'William Hills': {
            'WHH': 0,
            'WHD': 0,
            'WHA': 0,
        }
    }

    def __init__(self):
        self.betMarketManager = BetMarketManager()
        self.betManager = BetManager()

    def initialize_markets(self, line):
        labels = line.split(',')

        position = 0
        for label in labels:
            for key_market, value_markets in self.markets.items():
                for key_inner_market, value_inner_market in value_markets.items():
                    if label == key_inner_market:
                        self.markets[key_market][key_inner_market] = position

            position += 1

        for key_market, value_markets in self.markets.items():
            bet_market = self.betMarketManager.create_bet_market(key_market)
            bet_market.save()

    def create_ods(self, event, line):
        for key_market, value_markets in self.markets.items():
            for key_inner_market, value_inner_market in value_markets.items():
                if value_inner_market > 0:
                    if not BetMarket.objects.filter(name=key_market)[0]:
                        raise Exception('Market Not found')

                    bet = self.betManager.create_bet(
                        event.name,
                        self.get_bet(line, value_inner_market),
                        event.date,
                        BetMarket.objects.filter(name=key_market)[0],
                        self.find_type(key_inner_market), False)
                    event.bets.add(bet)
                    event.save()

    def get_bet(self, line, position):
        labels = line.split(',')
        return labels[position]

    def find_type(self, key):
        if key[-1:] == 'H':
            return BetType.objects.filter(identifier='H1')[0]
        elif key[-1:] == 'D':
            return BetType.objects.filter(identifier='TX')[0]
        elif key[-1:] == 'A':
            return BetType.objects.filter(identifier='A2')[0]
        else:
            raise Exception('Type Not Found')

    def get_player_home(self, line):
        labels = line.split(',')
        return labels[3]

    def get_player_away(self, line):
        labels = line.split(',')
        return labels[4]

    def get_date(self, line):
        # CREATE A DATE TIME UTIL
        labels = line.split(',')
        date = datetime.datetime.strptime(labels[1]+' '+labels[2], '%d/%m/%Y %H:%M')
        date.replace(tzinfo=timezone('UTC'))
        return date


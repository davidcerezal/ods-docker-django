from pprint import pprint
from django import template

from odds.domain.models.bet import Bet
from odds.domain.models.betType import BetType

register = template.Library()


@register.filter
def calculate_percentage(value, arg):
    value = 1 / value * (arg * 100)
    return '{:.2f}'.format(value)


@register.filter
def get_bet_by_type(value, type):
    for key, bet in value.items:
        if key == type:
            return bet

    return ''


@register.filter
def get_bet_type_trans(value):
    value = value.name if isinstance(value, BetType) else value
    if value == 'TX':
        return 'Empate'
    elif value == 'A2':
        return 'Visitante'
    else:
        return 'Casa'


@register.filter
def get_market_name(value):
    if isinstance(value, Bet):
        market = value.market.all()[0]
        return market.name
    else:
        return ''

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
    elif value == 'H1':
        return 'Local'
    elif value == '2partH1':
        return '2º tiempo local'
    elif value == '2partTX':
        return '2º tiempo empate'
    elif value == '2partA2':
        return '2º tiempo visitante'
    elif value == 'O1.5':
        return '+ 1.5 goles'
    elif value == 'U1.5':
        return '- 1.5 goles'
    elif value == 'O4.5':
        return '+ 4.5 goles'
    elif value == 'U4.5':
        return '- 4.5 goles'
    elif value == 'O5.5':
        return '+ 5.5 goles'
    elif value == 'U5.5':
        return '- 5.5 goles'
    elif value == 'O0.5':
        return '+ 0.5 goles'
    elif value == 'U0.5':
        return '- 0.5 goles'
    elif value == 'O2.5':
        return '+ 2.5 goles'
    elif value == 'U2.5':
        return '- 2.5 goles'
    elif value == 'O3.5':
        return '+ 3.5 goles'
    elif value == 'U3.5':
        return '- 3.5 goles'
    else:
        return 'None'

@register.filter
def get_market_name(value):
    if isinstance(value, Bet):
        market = value.market.all()[0]
        return market.name
    else:
        return ''

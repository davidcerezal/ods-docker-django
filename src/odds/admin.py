from django.contrib import admin

from .domain.models.apiImporter import ApiImporter
from .domain.models.bet import Bet
from .domain.models.betMarket import BetMarket
from .domain.models.betType import BetType
from .domain.models.sureBet import SureBet
from .domain.models.importResult import ImportResult
from .domain.models.event import Event

admin.site.register(Bet)
admin.site.register(BetMarket)
admin.site.register(BetType)
admin.site.register(ImportResult)
admin.site.register(SureBet)
admin.site.register(Event)
admin.site.register(ApiImporter)

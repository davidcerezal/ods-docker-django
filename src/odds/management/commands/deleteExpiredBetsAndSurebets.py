from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from odds.domain.models.bet import Bet
from odds.domain.models.sureBet import SureBet
from django.utils import timezone
from odds.domain.models.event import Event


class Command(BaseCommand):
    def handle(self, *args, **options):
        deleted = 0

        self.stdout.write(self.style.SUCCESS('Reviewing Surebets'))
        for surebet in SureBet.objects.all():
            if surebet.isExpired():
                surebet.delete()
                deleted += 1
        self.stdout.write(self.style.SUCCESS('Deleted "%s" surebets' % deleted))

        self.stdout.write(self.style.SUCCESS('Reviewing Bets'))
        for bet in Bet.objects.filter(expiry_date__lt=timezone.now()).all():
            if bet.isExpired():
                bet.delete()
                deleted += 1

        self.stdout.write(self.style.SUCCESS('Deleted "%s" in total' % deleted))

        self.stdout.write(self.style.SUCCESS('Reviewing Events'))
        for event in Event.objects.filter(date__lt=timezone.now()).all():
            if event.isExpired():
                event.delete()
                deleted += 1

        self.stdout.write(self.style.SUCCESS('Deleted "%s" in total' % deleted))

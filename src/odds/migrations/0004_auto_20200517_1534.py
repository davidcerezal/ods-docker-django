# Generated by Django 2.2.1 on 2020-05-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odds', '0003_auto_20200515_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='contra_bet',
            field=models.ManyToManyField(blank=True, related_name='_bet_contra_bet_+', to='odds.Bet'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='market',
            field=models.ManyToManyField(blank=True, to='odds.BetMarket'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='value',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='betmarket',
            name='api_key',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='betmarket',
            name='api_pass',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bettype',
            name='value',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.RemoveField(
            model_name='event',
            name='bets',
        ),
        migrations.AddField(
            model_name='event',
            name='bets',
            field=models.ManyToManyField(blank=True, to='odds.Bet'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='player1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='player2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.RemoveField(
            model_name='importresult',
            name='market',
        ),
        migrations.AddField(
            model_name='importresult',
            name='market',
            field=models.ManyToManyField(blank=True, to='odds.BetMarket'),
        ),
        migrations.AlterField(
            model_name='importresult',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='surebet',
            name='benefit',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='surebet',
            name='bets',
            field=models.ManyToManyField(blank=True, to='odds.Bet'),
        ),
        migrations.AlterField(
            model_name='surebet',
            name='value',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

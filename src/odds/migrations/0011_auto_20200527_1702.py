# Generated by Django 2.2.1 on 2020-05-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odds', '0010_auto_20200525_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surebet',
            name='revised',
            field=models.BooleanField(default=False),
        ),
    ]

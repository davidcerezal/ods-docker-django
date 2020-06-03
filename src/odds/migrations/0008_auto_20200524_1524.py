# Generated by Django 2.2.1 on 2020-05-24 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('odds', '0007_auto_20200524_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surebet',
            name='uuid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]

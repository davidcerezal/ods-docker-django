# Generated by Django 2.2.1 on 2020-06-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odds', '0011_auto_20200527_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiImporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('counter', models.FloatField(blank=True)),
                ('limit', models.FloatField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
    ]

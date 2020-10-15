# Generated by Django 3.1 on 2020-10-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prize',
            name='price_per_kill',
            field=models.FloatField(blank=True, help_text='Price per kill', null=True),
        ),
        migrations.AlterField(
            model_name='prize',
            name='winner_price',
            field=models.FloatField(blank=True, help_text='Price for winner at the end', null=True),
        ),
    ]
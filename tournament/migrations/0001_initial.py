# Generated by Django 3.1 on 2020-10-30 05:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('coremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.coremodel')),
                ('name', models.CharField(help_text='The name of prize', max_length=100)),
                ('icon', models.ImageField(default='default_prize.jpg', upload_to='')),
                ('price', models.FloatField(blank=True, help_text='Price', null=True)),
            ],
            bases=('accounts.coremodel',),
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The public name of the tournament', max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(default='default_tournament.jpg', upload_to='')),
                ('description', models.TextField(help_text='Match info')),
                ('instructions', models.TextField(help_text='Match Instructions')),
                ('password', models.CharField(help_text='Password for tournament', max_length=100)),
                ('kill_revenue', models.FloatField(default=0, help_text='Kill revenue')),
                ('starts_at', models.DateTimeField()),
                ('cost', models.FloatField(default=0, help_text='Match cost')),
                ('is_premium', models.BooleanField(default=False, help_text='Premium match')),
                ('max_players', models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('prizes', models.ManyToManyField(to='tournament.Prize')),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('coremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.coremodel')),
                ('cost', models.FloatField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournament.tournament')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
            bases=('accounts.coremodel',),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-20 16:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlistings_comments_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='users_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
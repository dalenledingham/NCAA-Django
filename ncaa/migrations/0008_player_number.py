# Generated by Django 3.2.5 on 2021-07-08 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncaa', '0007_player_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFavourite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfavourite',
            name='MyFavouriteName',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.13 on 2020-06-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200616_1704'),
        ('assets', '0005_auto_20200617_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetgroup',
            name='teams',
            field=models.ManyToManyField(blank=True, to='users.Team'),
        ),
    ]

# Generated by Django 2.2.13 on 2020-07-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='owner_username',
            field=models.TextField(default='n/a'),
        ),
    ]

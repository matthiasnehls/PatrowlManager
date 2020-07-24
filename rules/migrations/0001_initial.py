# Generated by Django 2.2.5 on 2019-09-17 23:07

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('comments', models.CharField(default='n/a', max_length=256)),
                ('scope', models.CharField(choices=[('asset', 'Asset'), ('finding', 'Finding'), ('scan', 'Scan')], default='finding', max_length=10)),
                ('scope_attr', models.CharField(blank=True, max_length=20, null=True)),
                ('condition', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('target', models.CharField(choices=[('event', 'Patrowl event'), ('logfile', 'To logfile'), ('email', 'Send email'), ('thehive', 'To TheHive (event'), ('splunk', 'To Splunk'), ('slack', 'To Slack')], default='event', max_length=10)),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=10)),
                ('trigger', models.CharField(choices=[('ondemand', 'On-demand'), ('auto', 'Auto'), ('periodic', 'Periodic')], default='auto', max_length=10)),
                ('trigger_attr', models.CharField(blank=True, max_length=20, null=True)),
                ('summary', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('nb_matches', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('periodic_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.PeriodicTask')),
            ],
            options={
                'db_table': 'rules',
            },
        ),
    ]

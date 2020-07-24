# Generated by Django 2.2.5 on 2019-09-17 23:07

import assets.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('ip', 'ip'), ('ip-range', 'ip-range'), ('ip-subnet', 'ip-subnet'), ('fqdn', 'fqdn'), ('domain', 'domain'), ('url', 'url'), ('keyword', 'keyword'), ('person', 'person'), ('organisation', 'organisation'), ('path', 'path'), ('application', 'application')], default='ip', max_length=15)),
                ('criticity', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='low', max_length=10)),
                ('risk_level', django.contrib.postgres.fields.jsonb.JSONField(default=assets.models.get_default_risk_level)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, default='new', max_length=30, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'assets',
            },
        ),
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256)),
                ('comments', models.CharField(blank=None, default='n/a', max_length=256, null=True)),
                ('parent', models.ForeignKey(blank=None, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='assets.AssetCategory')),
            ],
            options={
                'verbose_name_plural': 'Asset categories',
                'db_table': 'asset_categories',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AssetOwnerDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('doctitle', models.CharField(blank=True, max_length=256, null=True)),
                ('filename', models.CharField(blank=True, max_length=256, null=True)),
                ('filepath', models.CharField(blank=True, max_length=256, null=True)),
                ('tlp_color', models.CharField(choices=[('red', 'red'), ('amber', 'amber'), ('green', 'green'), ('white', 'white')], default='red', max_length=10)),
                ('comments', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asset_owner_docs',
            },
        ),
        migrations.CreateModel(
            name='AssetOwnerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('department', models.CharField(blank=True, max_length=256, null=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asset_owner_contacts',
            },
        ),
        migrations.CreateModel(
            name='AssetOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('assets', models.ManyToManyField(to='assets.Asset')),
                ('contacts', models.ManyToManyField(to='assets.AssetOwnerContact')),
                ('documents', models.ManyToManyField(to='assets.AssetOwnerDocument')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asset_owners',
            },
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('criticity', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default='None', max_length=10)),
                ('risk_level', django.contrib.postgres.fields.jsonb.JSONField(default=assets.models.get_default_risk_level)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('assets', models.ManyToManyField(to='assets.Asset')),
                ('categories', models.ManyToManyField(to='assets.AssetCategory')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'asset_groups',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='categories',
            field=models.ManyToManyField(to='assets.AssetCategory'),
        ),
        migrations.AddField(
            model_name='asset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

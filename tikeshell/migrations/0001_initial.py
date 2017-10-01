# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 10:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcomment', models.CharField(max_length=10)),
                ('text', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('iduser', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('idshow', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('imageurl', models.CharField(default=b'0', max_length=200)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(default=b'0', max_length=100)),
                ('tickets_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='showtype',
            fields=[
                ('idshowtype', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('showtype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='tickettype',
            fields=[
                ('tike_types', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('idticktype', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tikeshell.Show')),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='showtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tikeshell.showtype'),
        ),
        migrations.AddField(
            model_name='profile',
            name='event',
            field=models.ForeignKey(default=b'0', on_delete=django.db.models.deletion.CASCADE, to='tikeshell.Show'),
        ),
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tikeshell.Show'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
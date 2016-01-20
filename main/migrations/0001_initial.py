# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 05:46
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
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_timestamp', models.IntegerField()),
                ('end_timestamp', models.IntegerField()),
                ('subject', models.CharField(choices=[('Art', 'Art'), ('English', 'English'), ('History', 'History'), ('Math', 'Math'), ('Science', 'Science'), ('World Language', 'World Language'), ('Elective', 'Elective')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

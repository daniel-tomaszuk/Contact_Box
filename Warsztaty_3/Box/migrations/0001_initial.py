# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street', models.CharField(max_length=64)),
                ('house_number', models.IntegerField()),
                ('door_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[(1, 'Home Number'), (2, 'Work Number')], default=1, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Box.Address')),
                ('e_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Box.Email')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[(1, 'Home Number'), (2, 'Work Number')], default=1, max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='telephone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Box.Telephone'),
        ),
    ]
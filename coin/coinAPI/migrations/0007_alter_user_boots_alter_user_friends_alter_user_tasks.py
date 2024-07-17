# Generated by Django 5.0.6 on 2024-07-13 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinAPI', '0006_boots_remove_user_click_remove_user_energy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='boots',
            field=models.ForeignKey(blank=True, default=[], null=True, on_delete=django.db.models.deletion.CASCADE, to='coinAPI.boots'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, default=[], null=True, to='coinAPI.invitedfriends'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tasks',
            field=models.ManyToManyField(blank=True, default=[], null=True, to='coinAPI.tasks'),
        ),
    ]
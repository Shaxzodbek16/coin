# Generated by Django 5.0.6 on 2024-07-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinappAPI', '0005_user_add_per_tap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('voin', 'voin'), ('elite', 'elite'), ('master', 'master'), ('grandmaster', 'grandmaster'), ('epic', 'epic'), ('legend', 'legend'), ('mythic', 'mythic')], max_length=20),
        ),
    ]
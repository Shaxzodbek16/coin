# Generated by Django 5.0.6 on 2024-07-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinappAPI', '0007_remove_user_user_date_user_name_user_telegram_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='add_per_tap',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('voin', 'voin'), ('elite', 'elite'), ('master', 'master'), ('grandmaster', 'grandmaster'), ('epic', 'epic'), ('legend', 'legend'), ('mythic', 'mythic')], default='voin', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(max_length=15),
        ),
    ]

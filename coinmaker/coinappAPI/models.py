from django.db import models


class TelegramData(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)


class InvitedFriends(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    task_image = models.ImageField(upload_to='tasks_image/%Y/%m/')
    level = models.CharField(choices=(('E', 'Easy'), ('M', 'Medium'), ('W', 'Hard')), max_length=100)
    bonus = models.IntegerField()  # depending level


class User(models.Model):
    levels = (
        ('Pre-Beginner', 'Pre-Beginner'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Pre-Expert', 'Pre-Expert'),
        ('Expert', 'Expert'),
        ('Master', 'Master'),
        ('Champion', 'Champion'),
    )
    user_date = models.ForeignKey(TelegramData, on_delete=models.CASCADE)
    level = models.CharField(choices=levels, max_length=20)
    balance = models.PositiveBigIntegerField(default=0)
    boots = models.IntegerField(default=0)
    friends = models.ManyToManyField(InvitedFriends)
    last_updated = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Tasks)

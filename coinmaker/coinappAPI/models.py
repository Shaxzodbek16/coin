from django.db import models


class TelegramDate(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} with {self.telegram_id}"

    class Meta:
        db_table = 'telegram_date'
        verbose_name = 'telegram_date'
        verbose_name_plural = 'telegram_dates'


class InvitedFriends(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'invited_friend'
        verbose_name = 'invited_friend'
        verbose_name_plural = 'invited_friends'

    def __str__(self):
        return f"{self.name} with {self.telegram_id}"


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    task_image = models.ImageField(upload_to='tasks_image/%Y/%m/')
    level = models.CharField(choices=(('E', 'Easy'), ('M', 'Medium'), ('W', 'Hard')), max_length=100)
    bonus = models.IntegerField()  # depending level

    def __str__(self):
        return f"{self.task} with {self.bonus} at {self.level}"

    class Meta:
        db_table = 'task'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['level']


class User(models.Model):
    levels = (
        ('voin', 'voin'),
        ('elite', 'elite'),
        ('master', 'master'),
        ('grandmaster', 'grandmaster'),
        ('epic', 'epic'),
        ('legend', 'legend'),
        ('mific', 'mific'),
    )
    user_date = models.ForeignKey(TelegramDate, on_delete=models.CASCADE)
    level = models.CharField(choices=levels, max_length=20)
    balance = models.PositiveBigIntegerField(default=0)
    boots = models.IntegerField(default=0)
    friends = models.ManyToManyField(InvitedFriends)
    last_updated = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Tasks)

    def __str__(self):
        return f"{self.user_date} {self.level} {self.balance} {self.tasks}"

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['balance']

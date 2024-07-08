from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    bonus = models.IntegerField()

    def __str__(self):
        return f"{self.task} with {self.bonus} at {self.level}"

    class Meta:
        db_table = 'task'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ['level']


class User(models.Model):
    levels = (
        ('zero', 'zero'),
        ('voin', 'voin'),
        ('elite', 'elite'),
        ('master', 'master'),
        ('grandmaster', 'grandmaster'),
        ('epic', 'epic'),
        ('legend', 'legend'),
        ('mythic', 'mythic'),
    )

    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=15)
    level = models.CharField(choices=levels, default='zero', max_length=15)
    balance = models.PositiveBigIntegerField(default=0)
    boots = models.IntegerField(default=6)
    friends = models.ManyToManyField(InvitedFriends, null=True, blank=True)
    last_active = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Tasks, blank=True, null=True)
    passive = models.PositiveBigIntegerField(default=0)
    login_time = models.DateTimeField(auto_now_add=True)
    add_per_tap = models.PositiveIntegerField(default=10)

    LEVEL_THRESHOLDS = {
        'zero': 0,
        'voin': 1_000,
        'elite': 10_000,
        'master': 50_000,
        'grandmaster': 100_000,
        'epic': 1_000_000,
        'legend': 10_000_000,
        'mythic': 10_000_000_000_000_000
    }

    @property
    def next_level(self) -> str:
        for level, threshold in self.LEVEL_THRESHOLDS.items():
            if self.balance+1 <= threshold:
                return level
        return 'mythic'

    def __str__(self) -> str:
        return f"{self.name} --- {self.level} --- {self.balance}"

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['balance']

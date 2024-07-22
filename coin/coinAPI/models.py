from django.db import models


class InvitedFriends(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} with {self.telegram_id}"


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    task_image = models.ImageField(upload_to='tasks_image/%Y/%m/')
    level = models.CharField(choices=(('E', 'Easy'), ('M', 'Medium'), ('W', 'Hard')), max_length=100)
    bonus = models.IntegerField()

    def __str__(self):
        return f"{self.task} with {self.bonus} at {self.level}"


class User(models.Model):
    voin, elite, master, grandmaster, epic, legend, mythic = 'voin', 'elite', 'master', 'grandmaster', 'epic', 'legend', 'mythic'
    levels = ((voin, 'voin'), (elite, 'elite'), (master, 'master'), (grandmaster, 'grandmaster'), (epic, 'epic'),
              (legend, 'legend'), (mythic, 'mythic'))
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=20)
    level = models.CharField(choices=levels, default='voin', max_length=15)
    balance = models.PositiveBigIntegerField(default=0)
    friends = models.ManyToManyField(InvitedFriends, blank=True, null=True)
    last_active = models.DateTimeField(auto_now_add=True)
    tasks = models.ManyToManyField(Tasks, blank=True, null=True)
    passive = models.PositiveBigIntegerField(default=0)
    login_time = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(default=2)
    energy = models.IntegerField(default=6)
    boots = models.IntegerField(default=6)
    lv_up_amount = models.PositiveBigIntegerField(default=500)

    def __str__(self) -> str:
        return f"{self.name} --- {self.level} --- {self.balance}"

    @staticmethod
    def next_level(user_level: str, user_balance: int) -> bool | str:
        """
        increase user level depending on user_balance
        :param user_level:
        :param user_balance:
        :return: next level or False
        """

        levels = ('voin', 'elite', 'master', 'grandmaster', 'epic', 'legend', 'mythic')
        for i, lv in enumerate(levels):
            if user_level == lv:
                try:
                    user_level = levels[i + 1]
                    return user_level
                except IndexError:
                    return False

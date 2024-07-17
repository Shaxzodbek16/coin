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


class Boots(models.Model):
    click = models.IntegerField(default=2)
    energy = models.IntegerField(default=6)
    boots = models.IntegerField(default=6)

    def __str__(self):
        return f"{self.click} {self.energy} {self.boots}"


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
    boots = models.ForeignKey(Boots, on_delete=models.CASCADE, blank=True, null=True)
    lv_up_amount = models.PositiveBigIntegerField(default=500)

    def __str__(self) -> str:
        return f"{self.name} --- {self.level} --- {self.balance}"

    def next_level(self, user_level: str) -> bool | str:
        """
        increase user level
        :param user_level:
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

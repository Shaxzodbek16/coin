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
    status = models.BooleanField(default=False)

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
    level_img = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.name} --- {self.level} --- {self.balance}"

    def next_level(self, user_level: str) -> bool | str:
        levels = ('voin', 'elite', 'master', 'grandmaster', 'epic', 'legend', 'mythic')
        for i, lv in enumerate(levels):
            if user_level == lv:
                try:
                    user_level = levels[i + 1]
                    return user_level
                except IndexError:
                    return False

    def next_level_(self, user_level: str, user_balance: int | float, img: int) -> tuple[str | bool, int | bool]:
        coins_and_levels = {'voin': 1e3, 'elite': 1e4, 'master': 1e5, 'grandmaster': 1e6, 'epic': 1e7, 'legend': 1e8,
                            'mythic': 1e9}
        is_up = coins_and_levels.get(user_level)
        if user_balance > is_up:
            img += 1
            user_level = self.next_level(user_level)
            return user_level, img
        return False, False

    def complete_task(self, task):
        if task in self.tasks.all() and not task.status:
            task.status = True
            task.save()
            self.balance += task.bonus
            self.save()
            return True
        return False

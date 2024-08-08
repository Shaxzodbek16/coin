from django.test import TestCase, client
from .models import User, Tasks, InvitedFriends
from .serializers import UserSerializer, TasksSerializer, InvitedFriendsSerializer


class CoinAppAPITests(TestCase):
    def setUp(self):
        self.client = client
        pass


class UserTasksTestCase(TestCase):
    def setUp(self):
        # Test uchun foydalanuvchi yaratamiz
        self.user = User.objects.create(
            name="Test User",
            telegram_id="123456789",
            level="voin",
            balance=1000
        )

        # Test uchun task yaratamiz
        self.task_easy = Tasks.objects.create(
            task="Easy Task",
            level="E",
            bonus=100,
            status=False
        )

        self.task_medium = Tasks.objects.create(
            task="Medium Task",
            level="M",
            bonus=200,
            status=False
        )

        self.task_hard = Tasks.objects.create(
            task="Hard Task",
            level="W",
            bonus=300,
            status=False
        )

        # Tasklarni foydalanuvchiga bog'laymiz
        self.user.tasks.add(self.task_easy, self.task_medium, self.task_hard)

    def test_complete_easy_task(self):
        # Foydalanuvchi oson taskni bajaradi
        result = self.user.complete_task(self.task_easy)

        # Natijalarni tekshiramiz
        self.assertTrue(result)
        self.assertEqual(self.user.balance, 1100)
        self.assertTrue(self.task_easy.status)

    def test_complete_medium_task(self):
        # Foydalanuvchi o'rtacha taskni bajaradi
        result = self.user.complete_task(self.task_medium)

        # Natijalarni tekshiramiz
        self.assertTrue(result)
        self.assertEqual(self.user.balance, 1200)
        self.assertTrue(self.task_medium.status)

    def test_complete_hard_task(self):
        # Foydalanuvchi qiyin taskni bajaradi
        result = self.user.complete_task(self.task_hard)

        # Natijalarni tekshiramiz
        self.assertTrue(result)
        self.assertEqual(self.user.balance, 1300)
        self.assertTrue(self.task_hard.status)
from django.test import TestCase, client
from .models import User, Boots, Tasks, InvitedFriends
from .serializers import UserSerializer, BootsSerializer, TasksSerializer, InvitedFriendsSerializer


class CoinAppAPITests(TestCase):
    def setUp(self):
        self.client = client
        pass

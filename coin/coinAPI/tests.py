from django.test import TestCase, client
from .models import User, Tasks, InvitedFriends
from .serializers import UserSerializer, TasksSerializer, InvitedFriendsSerializer


class CoinAppAPITests(TestCase):
    def setUp(self):
        self.client = client
        pass

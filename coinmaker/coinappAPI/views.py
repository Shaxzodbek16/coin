from django.shortcuts import render
from .models import User, InvitedFriends, TelegramData, Tasks
from .serializers import UserSerializer, InvitedFriendsSerializer, TelegramDataSerializer, TasksSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


class UserAPIView(APIView):
    pass


class InvitedFriendsAPIView(APIView):
    pass


class TelegramDataAPIView(APIView):
    pass


class TasksAPIView(APIView):
    pass

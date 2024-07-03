from rest_framework import serializers
from .models import User, InvitedFriends, TelegramData, Tasks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class InvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedFriends
        fields = '__all__'
        read_only_fields = ('id',)


class TelegramDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramData

        fields = '__all__'
        read_only_fields = ('id',)


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ('id',)

from rest_framework import serializers
from .models import User, InvitedFriends, Tasks


class InvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedFriends
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True, required=False)
    invited_friends = InvitedFriendsSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        return user


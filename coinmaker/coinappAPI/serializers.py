from rest_framework import serializers
from .models import User, InvitedFriends, Tasks


class InvitedFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitedFriends
        fields = '__all__'
        read_only_fields = ('id',)


class TasksSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        return f"https://coin.shaxzodbek.com{obj.task_image.url}"

    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    # friends = InvitedFriendsSerializer(many=True)
    # tasks = TasksSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)

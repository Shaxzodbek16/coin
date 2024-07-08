from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User, InvitedFriends, Tasks, post_save
from django.db.models import F
from .serializers import UserSerializer, InvitedFriendsSerializer, TasksSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response


class UserAPIView(APIView):
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['level']
    ordering_fields = ['balance']

    def get_queryset(self):
        queryset = User.objects.all()
        level = self.request.query_params.get('level')
        if level:
            queryset = queryset.filter(level=level)
        return queryset

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            if self.request.query_params.get('boots'):
                user_boots = User.objects.get(pk=pk).boots
                if user_boots > 0:
                    user_boots -= 1
                user = User.objects.get(pk=pk)
                user.update(boots=user_boots)
                user.save()
            try:
                user = User.objects.get(pk=pk)
                user.balance += user.add_per_tap
                next_level = user.next_level
                user.level = next_level
                user.save()
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        filter_backends = (DjangoFilterBackend, OrderingFilter)
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": " not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": " not found"}, status=status.HTTP_404_NOT_FOUND)


class InvitedFriendsAPIView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                friend = InvitedFriends.objects.get(pk=pk)
                serializer = InvitedFriendsSerializer(friend)
                return Response(serializer.data)
            except InvitedFriends.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        friends = InvitedFriends.objects.all()
        serializer = InvitedFriendsSerializer(friends, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvitedFriendsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            friend = InvitedFriends.objects.get(pk=pk)
        except InvitedFriends.DoesNotExist:
            return Response({"error": "friends not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvitedFriendsSerializer(friend, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            friend = InvitedFriends.objects.get(pk=pk)
            friend.delete()
            return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except InvitedFriends.DoesNotExist:
            return Response({"error": "friend not found"}, status=status.HTTP_404_NOT_FOUND)


class TasksAPIView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                task = Tasks.objects.get(pk=pk)
                serializer = TasksSerializer(task)
                return Response(serializer.data)
            except Tasks.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            task = Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            return Response({"error": "friends not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TasksSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            task = Tasks.objects.get(pk=pk)
            task.delete()
            return Response({"message": f"telegram_date successfully deleted with {pk} id"},
                            status=status.HTTP_204_NO_CONTENT)
        except Tasks.DoesNotExist:
            return Response({"error": f"friend not found with {pk} id"}, status=status.HTTP_404_NOT_FOUND)

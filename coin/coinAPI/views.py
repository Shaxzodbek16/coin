import time

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User, InvitedFriends, Tasks
from .serializers import UserSerializer, TasksSerializer, InvitedFriendsSerializer
from django.db.models import ManyToManyRel


class UserAPIView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            click = request.query_params.get('click', False)
            energy = request.query_params.get('energy', False)
            stop_energy = request.query_params.get('stop_energy', False)
            boots = request.query_params.get('boots', False)
            increase_balance = request.query_params.get('increase_balance', False)
            if increase_balance == 'True':
                user.balance = user.balance + user.click
                user.save()
            if click == "True":
                if user.balance >= user.lv_up_amount:
                    user.balance -= user.lv_up_amount
                    user.lv_up_amount = user.lv_up_amount * 1.2
                    user.lv_up_amount = int(user.lv_up_amount)
                    user.click = user.click + 1
                    user.save()
                return Response({"message": "Not enaught coin to click up"}, status=status.HTTP_400_BAD_REQUEST)
            if energy == "True":
                user.click = user.click * 2
                user.energy -= 1
                user.save()
            if stop_energy == "True":
                user.click = user.click // 2
                user.save()
            if boots == "True":
                pass
            level = user.next_level(user.level, user.balance)
            if level is not False:
                user.level = level
                user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Successfully created by:\n {serializer.data}'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        if pk:
            serializer = UserSerializer(User.objects.get(pk=pk), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': f'Succesfully changed by {pk} id'}, status=status.HTTP_200_OK)
            return Response({'message': f'user not found by {pk} id'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        if pk:
            user = User.objects.get(pk=pk)
            name = user.name
            user.delete()
            return Response({'message': f'Succesfully deleted {name} by {pk} id'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': f'user not found by {pk} id'}, status=status.HTTP_400_BAD_REQUEST)

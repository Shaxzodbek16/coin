from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User, InvitedFriends, Tasks, Boots
from .serializers import UserSerializer, BootsSerializer, TasksSerializer, InvitedFriendsSerializer


class UserAPIView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            serializer = UserSerializer(User.objects.get(pk=pk))
            click_up = request.query_params.get('click_up', False)
            energy = request.query_params.get('energy', False)
            boots = request.query_params.get('boots', False)
            # hali ko'p logika
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': f'Successfully created by:\n {serializer.data}'}, status=status.HTTP_201_CREATED)
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

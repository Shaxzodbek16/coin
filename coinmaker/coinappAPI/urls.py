from django.urls import path
from .views import UserAPIView, InvitedFriendsAPIView, TelegramDateAPIView, TasksAPIView
urlpatterns = [
    path('api/user/', UserAPIView.as_view(), name='user'),
    path('api/friends/', InvitedFriendsAPIView.as_view(), name='friends'),
    path('api/tasks/', TasksAPIView.as_view(), name='tasks'),
    path('api/telegram/', TelegramDateAPIView.as_view(), name='telegram'),
    path('api/user/<int:pk>/', UserAPIView.as_view(), name='user-pk'),
    path('api/tasks/<int:pk>/', TasksAPIView.as_view(), name='tasks-pk'),
    path('api/friends/<int:pk>/', InvitedFriendsAPIView.as_view(), name='friends-pk'),
    path('api/telegram/<int:pk>/', TelegramDateAPIView.as_view(), name='telegram-pk'),
]

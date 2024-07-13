from django.urls import path
from .views import UserAPIView
urlpatterns = [
    path('api/user/<int:pk>/', UserAPIView.as_view(), name='user-pk'),
    path('api/user/', UserAPIView.as_view(), name='user'),

]

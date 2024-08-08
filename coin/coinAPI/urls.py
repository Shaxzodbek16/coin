from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('api/user/<int:pk>/', UserAPIView.as_view(), name='user-pk'),
    path('api/user/', UserAPIView.as_view(), name='user'),
    # URLlarga taskni bajarishni qo'shamiz
    #  /api/user/1/?click=True Bu click ni ko'taradi, balancega qaridi, narxi oshib boradi.
    #  /api/user/1/?energy=True Bu clickni 2x qib berdi
    #  /api/user/1/?stop_energy=True Bu clickni 1/5x qib berdi
    #  /api/user/1/?increase_balance=True Bu balancega clickni qo'shadi
    #  /api/user/1/?task_complete=task_id Bu taskni bajaradi va bonusni balansga qo'shadi
]

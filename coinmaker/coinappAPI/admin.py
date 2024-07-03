from django.contrib import admin
from .models import User, InvitedFriends, TelegramData, Tasks


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    all = ['level', 'balance', 'boots', 'last_updated']
    list_display, list_filter, search_fields = all, all, all


@admin.register(InvitedFriends)
class InvitedFriendsAdmin(admin.ModelAdmin):
    all = ['name', 'telegram_id']
    list_display, list_filter, search_fields = all, all, all


@admin.register(TelegramData)
class TelegramDataAdmin(admin.ModelAdmin):
    all = ['name', 'telegram_id']
    list_display, list_filter, search_fields = all, all, all


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    all = ['task', 'level', 'bonus']
    list_display, list_filter, search_fields = all, all, all

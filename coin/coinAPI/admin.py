from django.contrib import admin
from .models import User, Tasks, InvitedFriends


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    all_per = ('name', 'telegram_id', 'level', 'balance', 'last_active', 'passive', 'login_time', 'lv_up_amount')
    list_display = all_per
    search_fields = all_per
    list_filter = all_per


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('task', 'task_image', 'level', 'bonus', 'status')
    search_fields = ('task', 'level')
    list_filter = ('level', 'status')


@admin.register(InvitedFriends)
class InvitedFriendsAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_id')
    search_fields = ('name', 'telegram_id')
    list_filter = ('name',)



# admin.site.register(User, UserAdmin)
# admin.site.register(Tasks, TasksAdmin)
# admin.site.register(InvitedFriends, InvitedFriendsAdmin)

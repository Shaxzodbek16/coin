from .models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    all_per = ('name', 'telegram_id', 'level', 'balance', 'last_active', 'passive', 'login_time', 'lv_up_amount')
    list_display, search_fields, list_filter = all_per, all_per, all_per

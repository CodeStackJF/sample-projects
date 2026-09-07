from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('password', 'salt', 'created_at')
    ordering = ('-created_at',)
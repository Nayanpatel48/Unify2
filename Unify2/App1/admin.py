from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # Update list_display to match the fields that exist in your custom User model
    list_display = ('email', 'name', 'role', 'is_active', 'is_staff', 'profile_picture','password')  # 'user_id' and 'created_at' should be removed if not present
    list_filter = ('role', 'is_active', 'is_staff')  # 'created_at' should be removed if not present
    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(User, UserAdmin)

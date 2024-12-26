from django.contrib import admin

# Register your models here.
from django.contrib import admin

# The UserProfile model is imported from the models.py file in the same app.
from .models import UserProfile, Item

# The @admin.register(UserProfile) decorator registers the UserProfile model 
# with the Django Admin site.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [ 'username', 'email', 'phone_number', 'created_at']
# UserProfileAdmin is a class that inherits from admin.ModelAdmin.
# It allows customization of how the UserProfile model is displayed and managed 
# in the Django Admin interface.
# The list_display attribute specifies which fields of the UserProfile model should
# be shown in the list view of the Admin panel.
# Each element in the list corresponds to a field in the UserProfile model.
# same is true for 'ItemAdmin' function

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['name', 'description', 'price', 'uploaded_by', 'created_at']
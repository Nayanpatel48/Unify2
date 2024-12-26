from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
# In Django models are python classes that represents the structure of your database tables.
# They act as a bridge between your python code and the underlying database, allowing you 
# to define and interact with your databse in an object-oriented manner.
from django.utils.timezone import now 
from django.db import models

from django.contrib.auth.models import User
# Django's built in model for managing user authentication and user-related operations

class UserProfile(models.Model):
    # here unique field in the django parameters ensures that the value is unique accross 
    # all rrecords in the database
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # Specifies the directory within the MEDIA_ROOT folder where uploaded images will be stored.
    # For example, if MEDIA_ROOT is set to /media/ in your settings, the uploaded images will be 
    # saved in /media/profile_images/.

    # created_at = models.DateTimeField(auto_now_add=True)
    # Automatically sets the field to the current date and time when the record is created.

    def __str__(self):
        return self.username
    # special method in django which defines the "string representation of object."
    # used in many places one of them is django admin panel for viewing
    
# This class represents an item or product in the database.
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_items")
    
    created_at = models.DateTimeField(auto_now_add=True)
    # Stores the timestamp when the item was created.

    def __str__(self):
        return self.name
    def __str__(self):
        return self.username

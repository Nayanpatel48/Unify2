from django.urls import path, include
from . import views  # Import views from the current app

from django.contrib import admin
# imports django's built-in admin panel

from django.conf.urls.static import static
# used to serve the static and media files in development.

urlpatterns = [
    path('admin/', admin.site.urls),

    # passwing transfer to APP1
    path('' , include('App1.urls')),
]
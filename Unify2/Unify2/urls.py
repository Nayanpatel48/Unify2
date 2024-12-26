from django.urls import path
from . import views  # Import views from the current app

from django.contrib import admin
# imports django's built-in admin panel

from django.conf import settings 
# imported project settings which are used to configure things like media files.

from django.urls import path, include
# path is used to define url patterns, 
# "include" is used to include URL configurations from other django apps.

from django.conf.urls.static import static
# used to serve the static and media files in development.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    # whenever i am hitting this url i am transfering control to an app urls
    # Routes all URLs starting with http://127.0.0.1:8000/login/ to the login app.
    # The login.urls file defines the routes for the app. 
    # path('register/', include('subapp.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
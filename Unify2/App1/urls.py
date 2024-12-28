from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  
# from .views import homepage, layout2, register, login_view

urlpatterns = [

    path('', views.homepage, name='homepage'),

    path('layout2/', views.layout2, name='layout2'),

    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [

    # http://127.0.0.1:8000/ is homepage 
    path('', views.homepage, name='homepage'),

    path('layout2/', views.layout2, name='layout2'),
]
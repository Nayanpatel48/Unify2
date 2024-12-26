from django.urls import path
# path is used to define url patterns

from django.contrib.auth import views as auth_views
# auth_views contains prebuilt class-based views for authentication and password management.

from . import views
# imported views, this views are classes or functions which handles the request for specific
# urls

urlpatterns = [
    path('', views.register, name='register'),
    # This URL is for the register page of the application.
    # Example: Accessing http://127.0.0.1:8000/register/ will display the register form.
    
    path('success/', views.success, name='success'),
    # this URL is for the registration success page.
    # Example: Accessing http://127.0.0.1:8000/success_page/ will display success page.

    path('user_list/', views.user_list, name='user_list'),
    # redirect to user_list page whenever this url has hitted

    path('login/', views.login_view, name='login'),
    # redirect to login page whenever this url has been hitted or queried

    path('dashboard/', views.dashboard_view, name='dashboard'),
    # redirect to dashboard page whenever this url has been hitted or queried

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # displays a form where user enters their details for password reset request.

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # desplays the success message after user submits the password reset request.

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # displays a from where user can enter a new password

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # displays a success message after user successfully resets the password

    path('logout/', views.logout_view, name = 'logout'),
    # when ever /logout/ hitted logout page is will be displayed

    path('search/', views.search_items, name='search_items'),
    
    path('upload/', views.upload_item, name='upload_item'),
]
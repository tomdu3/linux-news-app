from django.urls import path, include
from . import views
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]

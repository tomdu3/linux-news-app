from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/user_page', views.user_page, name='user_page'),
    ]
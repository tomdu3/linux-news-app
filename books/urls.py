from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_page/', views.user_page, name='user_page'),
    path('user_favourites/', views.user_favourites, name='user_favourites'),
    path('summernote/', include('django_summernote.urls')),
    path('details/<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    ]
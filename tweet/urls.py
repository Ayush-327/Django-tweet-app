from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tweet_list, name='tweet_list'),
    path('<int:tweet_id>/edit/', views.Tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete', views.Tweet_delete, name='tweet_delete'),
    path('create/', views.Tweet_create, name='tweet_create'),
    path('register/', views.register, name='register'),
] 
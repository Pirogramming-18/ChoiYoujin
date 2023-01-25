from django.urls import path
from . import views

app_name = 'pirostagram'
urlpatterns = [
    path('', views.post_feed, name = 'post_feed'),
    path('<int:pk>/post_detail/', views.post_detail, name = 'post_detail'),
    path('post_like_ajax/', views.post_like_ajax, name = 'post_like'),
    path('comment_add_ajax/', views.comment_add_ajax, name = 'comment_add'),
    path('comment_delete_ajax/', views.comment_delete_ajax, name = 'comment_delete'),
]
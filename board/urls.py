from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='post'),
    path('post_new/', views.post_new, name='post_new'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
]
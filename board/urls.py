from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='board_home'),
    path('new/', views.new, name='board_new'),
    path('detail/<int:board_id>', views.detail, name='board_detail'),
]
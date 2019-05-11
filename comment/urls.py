from django.urls import path
from . import views

urlpatterns = [
    path('board/new', views.board_new, name='comment_board_new'),
    path('board/delete', views.board_delete, name='comment_board_delete'),
    path('lost/new', views.lost_new, name='comment_lost_new'),
    path('lost/delete', views.lost_delete, name='comment_lost_delete'),
]
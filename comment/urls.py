from django.urls import path
from . import views

urlpatterns = [
    path('board/new', views.board_new, name='board_new'),
    path('board/delete', views.board_delete, name='board_delete'),
    # path('lost/new', views.lost_new, name='lost_new'),
    path('lost/delete', views.lost_delete, name='lost_delete'),
]
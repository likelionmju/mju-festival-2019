from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('board/new', views.board_new, name='board_new'),
    path('board/delete', views.board_delete, name='board_delete'),
    # path('lost/new', views.lost_new, name='lost_new'),
    path('lost/delete', views.lost_delete, name='lost_delete'),
=======
    path('board/new', views.board_new, name='comment_board_new'),
    path('board/delete', views.board_delete, name='comment_board_delete'),
    path('lost/new', views.lost_new, name='comment_lost_new'),
    path('lost/delete', views.lost_delete, name='comment_lost_delete'),
>>>>>>> 05ddc714b2ab5ebc4edd0110de9c9a78ea86f0ca
]
from django.urls import path
from . import views

urlpatterns = [
    path('board/<int:board_id>/new', views.board_new, name='comment_board_new'),
    path('board/<int:board_id>/delete/<int:comment_id>', views.board_delete, name='comment_board_delete'),
    path('lost/<int:stuff_id>/new/', views.lost_new, name='comment_lost_new'),
    path('lost/<int:stuff_id>/delete/<int:comment_id>', views.lost_delete, name='comment_lost_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lost_home'),
    path('new/', views.new, name='lost_new'),
    path('detail/<int:stuff_id>', views.detail, name='lost_detail'),
    path('delete/<int:stuff_id>', views.delete, name='lost_delete'),
    path('edit/<int:stuff_id>', views.edit, name='lost_edit'),
]
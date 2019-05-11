from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lost_home'),
    path('new/', views.new, name='lost_new'),
    path('detail/<int:lost_id>', views.detail, name='lost_detail'),
]



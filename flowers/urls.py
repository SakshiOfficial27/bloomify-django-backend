from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/flowers/', views.flower_list, name='flower_list'),
    path('api/flowers/<int:pk>/', views.update_flower, name='update_flower'),
    path('api/flowers/delete/<int:pk>/', views.delete_flower, name='delete_flower'),
]
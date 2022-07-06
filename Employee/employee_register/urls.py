
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee,name='list'),
    path('register/', views.register_employee,name='register'),
    path('update/<int:pk>/', views.update_employee,name='update'),
    path('delete/<int:pk>/', views.delete_employee,name='delete'),
    
    
]
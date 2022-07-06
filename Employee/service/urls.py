from django.urls import path
from .import views

urlpatterns = [
    path('',views.user_login_view,name='login'),
    path('signup/',views.user_register_view,name='signup'),
]

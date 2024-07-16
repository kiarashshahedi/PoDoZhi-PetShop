from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addresses/', views.manage_addresses, name='manage_addresses'),
    path('order-history/', views.order_history, name='order_history'),
]

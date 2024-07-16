from django.urls import path
from . import views

urlpatterns = [
    
    # home page
    path('', views.product_list, name='home_product_list'),
    
    # product detail page
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    # navbar category list
    path('navbar/', views.navbar, name='navbar'),

    # main and sub Categories pages
    path('main-category/<int:main_category_id>/', views.main_category_view, name='main_category'),
    path('sub-category/<int:sub_category_id>/', views.sub_category_view, name='sub_category'),
    
]

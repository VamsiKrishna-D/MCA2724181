from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
    path('products/', views.product_list, name='product_list'),
    
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html',redirect_authenticated_user=True),name='login'), 
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    
]



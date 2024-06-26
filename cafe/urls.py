from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('products/', views.products, name='products'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('manage_storage/', views.manage_storage, name='manage_storage'),
    path('add_product/', views.add_product, name='add_product'),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('api/top-selling-products/', views.top_selling_products_api, name='top_selling_products_api'),
]

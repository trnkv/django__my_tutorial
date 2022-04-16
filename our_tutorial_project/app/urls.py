from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all_products', views.get_all_products, name='get_all_products'),
    path('add_product_to_cart', views.add_product_to_cart, name='add_product_to_cart'),
]
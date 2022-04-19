from math import prod
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import *


def index(request):
    return render(request, 'index.html', context={})


def show_cart(request):
    this_user = request.user
    user_cart = Cart.objects.get(user=this_user)
    user_products = user_cart.product.all()
    result = {}
    for product in user_products:
        result[product.category.name] = {
            'id': product.id,
            'name': product.name,
            'price': product.price
        }
    return render(request, 'cart.html', context={'result': result})


def get_all_products(request):
    all_products = Product.objects.all()
    result = []
    for product in all_products:
        result.append(
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'category': product.category.name
            }
        )
    return JsonResponse(result, safe=False)


def add_product_to_cart(request):
    product_id = request.GET.get('product_id')
    
    this_user = request.user
    this_user_cart = Cart.objects.get(user=this_user)
    this_user_cart.product.add(product_id)
    
    return HttpResponse(status=200)


def delete_a_product(request):
    product_id = request.GET.get('product_id')
    this_user = request.user
    this_user_cart = Cart.objects.get(user=this_user)
    this_user_cart.product.remove(product_id)
    return HttpResponse(status=200)
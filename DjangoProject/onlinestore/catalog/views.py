from os import name

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Product, Category


# Create your views here.

def product_list(request):
    products = Product.objects.all()

    data = list(products.values('id', 'name', 'description', 'price', 'category__name'))
    return JsonResponse(data, safe=False)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    data = {
        'id' : product.id,
        'name' : product.name,
        'description' : product.description,
        'count' : product.count,
        'price' : float(product.price),
        'category' : product.category.name
    }

    return JsonResponse(data)

def category_list(request):
    categories = Category.objects.all()

    data = list(categories.values('id', 'name', 'description'))

    return JsonResponse(data, safe=False)

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)

    data = {
        'name' : category.name
    }

    return JsonResponse(data)

def products_by_category(request, pk):
    category = get_object_or_404(Category, id = pk)

    products = Product.objects.filter(category=category, is_active=True)

    data = list(products.values('id', 'name', 'description', 'price', 'category__name'))

    return JsonResponse(data, safe=False)
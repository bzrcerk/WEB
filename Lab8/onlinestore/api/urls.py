from django.contrib import admin
from django.urls import path

from catalog.views import product_list, product_detail, category_list, category_detail, products_by_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', product_list, name='product_list'),
    path('api/products/<int:pk>/', product_detail, name='product_detail'),
    path('api/categories/', category_list, name='category_list'),
    path('api/categories/<int:pk>/', category_detail, name='category_detail'),
    path('api/categories/<int:pk>/products/', products_by_category, name='products_by_category'),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from catalog.views import ProductsViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

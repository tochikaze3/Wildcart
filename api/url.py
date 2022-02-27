from django.urls import path
from .views import UserViewSet, ProductViewSet,ProductImageViewSet, VendorViewSet, CategoryViewSet, ServiceViewSet
from rest_framework import routers

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendors') 
router.register(r'products', ProductViewSet, basename='products')
router.register(r'services', ServiceViewSet, basename='services') 
router.register(r'productimages', ProductImageViewSet, basename='productimages')
router.register(r'categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

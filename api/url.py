from django.urls import path
from .views import ProductViewSet,ProductImageViewSet, VendorViewSet, CategoryViewSet
from rest_framework.routers import SimpleRouter

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = SimpleRouter()
router.register('vendors', VendorViewSet, basename='vendors') 
router.register('products', ProductViewSet, basename='products')
router.register('productimages', ProductImageViewSet, basename='productimages')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls

from django.urls import path
from .views import UserViewSet, ProductViewSet,ProductImageViewSet, VendorViewSet, CategoryViewSet
from rest_framework.routers import SimpleRouter

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = SimpleRouter()
router.register('vendors/', VendorViewSet, base_name='vendors') 
router.register('products/', ProductViewSet, base_name='products')
router.register('productimages/', ProductImageViewSet, base_name='productimages')
router.register('categories/', CategoryViewSet, base_name='categories')

urlpatterns = router.urls

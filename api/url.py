from django.urls import path
from .views import ProductViewSet,ProductImageViewSet, VendorViewSet, CategoryViewSet
from rest_framework.routers import SimpleRouter

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = SimpleRouter()
router.register('vendors/', VendorViewSet) 
router.register('products/', ProductViewSet)
router.register('productimages/', ProductImageViewSet)
router.register('categories/', CategoryViewSet)

urlpatterns = router.urls

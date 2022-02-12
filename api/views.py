from rest_framework import viewsets
#from .permissions import IsAuthorOrReadOnly
from stores.models import Vendor, Category, Products, ProductImage
from .serializers import VendorSerializer,ProductSerializer, CategorySerializer, ProductImageSerializer


 
#user views
#class UserList(generics.ListCreateAPIView): 
#        queryset = CustomUser.objects.all() 
 #       serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
        #queryset = CustomUser.objects.all()
        #serializer_class = UserSerializer

class VendorViewSet(viewsets.ModelViewSet):
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet): # new permission_classes = (IsAuthorOrReadOnly,) 
        queryset = ProductImage.objects.all() 
        serializer_class = ProductImageSerializer

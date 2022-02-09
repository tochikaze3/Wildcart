
from rest_framework import viewsets, generics
#from .permissions import IsAuthorOrReadOnly
from stores.models import Vendor, Category, Products
from .serializers import VendorSerializer,ProductSerializer, CategorySerializer


 
#user views
#class UserList(generics.ListCreateAPIView): 
#        queryset = CustomUser.objects.all() 
 #       serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
        #queryset = CustomUser.objects.all()
        #serializer_class = UserSerializer

class VendorList(generics.ListCreateAPIView):
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer
        
   

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Vendor.objects.all()
        serializer_class = VendorSerializer


class CategoryList(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
   

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        


#buyer views
class ProductList(generics.ListCreateAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer
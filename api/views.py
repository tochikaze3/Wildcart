
from rest_framework import viewsets, generics
#from .permissions import IsAuthorOrReadOnly
from stores.models import Store, Category, Products
from .serializers import StoreSerializer,ProductSerializer, CategorySerializer


 
#user views
#class UserList(generics.ListCreateAPIView): 
#        queryset = CustomUser.objects.all() 
 #       serializer_class = UserSerializer

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
        #queryset = CustomUser.objects.all()
        #serializer_class = UserSerializer

class StoreList(generics.ListCreateAPIView):
        queryset = Store.objects.all()
        serializer_class = StoreSerializer
        
   

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Store.objects.all()
        serializer_class = StoreSerializer


class CategoryList(generics.ListAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
   

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        


#buyer views
class ProductList(generics.ListAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductSerializer
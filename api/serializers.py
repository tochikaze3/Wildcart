from rest_framework import serializers
from stores.models import Products, Category, Store

#vendor_api serializers
#class UserSerializer(serializers.ModelSerializer):
    
    #class Meta:
        #model = CustomUser() 
        #fields = ('id', 'email',)


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Store
        fields = '__all__'

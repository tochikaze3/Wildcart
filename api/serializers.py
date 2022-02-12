from dataclasses import field, fields
from rest_framework import serializers
from stores.models import Products, Category, Vendor, ProductImage

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

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Vendor
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer0):

    class Meta:
        model = ProductImage
        fields = '__all__'
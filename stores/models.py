from django.db import models
from accounts.models import Vendor 
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
    	return self.category


@staticmethod
def get_all_categories():
    return Category.objects.all()


class Products(models.Model):
        product_Name = models.CharField(max_length=250, help_text = 'Enter product name' )
        upload_Product_Image = models.ImageField(default='default.jpg')
        product_Description = models.CharField(default = '', max_length= 200)
        weight = models.CharField(max_length= 10, default = 'g/kg/lb', blank= True)

        Size_Status = (
            ('X', 'Small'),
            ('XX', 'Large'),
            ('XXL', 'Extra large'),
            )

        size = models.CharField(max_length=5, choices= Size_Status, blank= True, default='X')
        stock = models.IntegerField(default= 'Choose total number of goods available')
        price = models.DecimalField(max_digits=1000,  default= 00.00, decimal_places=2)
                
        
        def __str__(self):
            return self.product_Name

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.product
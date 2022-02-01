from uuid import uuid4
from django.db import models
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
        upload_Product_Image = models.ImageField(default='default.jpg', upload_to= 'profile_pic')
        product_Description = models.CharField(default = '', max_length= 200)
        weight = models.CharField(max_length= 10, default = 'g/kg/lb', blank= True)

        Size_Status = (
            ('X', 'Small'),
            ('XX', 'Large'),
            ('XXL', 'Extra large'),
            )
        Currency = (
            ('Naira Token','NGNT'),
            ('Dollar','USD'),
        )

        size = models.CharField(max_length=5, choices= Size_Status, blank= True, default='X')
        stock = models.IntegerField(default= 'Choose total number of goods available')
        currency = models.CharField(max_length= 11, choices= Currency, help_text='The Naira Token is a stablecoin tied to the value of the naira, in other words NGN200 = NGNT200', default= 00.00)
        price = models.DecimalField(max_digits=1000, decimal_places=2)
                
        
        def __str__(self):
            return self.product_Name


@staticmethod
def get_products_by_id(ids):
	return Products.objects.filter(id__in=ids)

@staticmethod
def get_all_products():
	return Products.objects.all()

@staticmethod
def get_all_products_by_categoryid(category_id):
	if category_id:
		return Products.objects.filter(category=category_id)
	else:
		return Products.get_all_products_by_categoryid()




class Store(models.Model):
    store_name = models.CharField(help_text= 'Your store name', default= '', max_length= 250)
    #products = models.ForeignKey(Products, on_delete=models.CASCADE,)
    email = models.EmailField(default= '', max_length= 250, help_text= 'Your email name')
    about = models.TextField(max_length=1000, help_text='Give a catchy description of your store', default= '')
    phone = models.CharField(max_length=20, default= "", null= False, blank= False)
    location = models.CharField(help_text= 'Enter your store location', default= '', max_length= 250)

    def __str__(self):
        return self.store_name

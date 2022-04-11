from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
    	return self.category


@staticmethod
def get_all_categories():
    return Category.objects.all()


class Products(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        product_Name = models.CharField(max_length=250, help_text = 'Enter product name' )
        upload_Product_Image = models.ImageField(default='default.jpg')
        product_Description = models.CharField(default = '', max_length= 200)
        weight = models.CharField(max_length= 100, default = 'kg', blank= True)

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
    images = models.FileField(upload_to = 'staticfiles/images')




class Vendor(models.Model):
    #user = models.OneToOneField(UserProfile, related_name='vendor', on_delete=models.CASCADE)
    store_name = models.CharField(help_text= 'Your store name', default= '', max_length= 250)
    logo = models.ImageField(upload_to = 'staticfiles/images')
    about = models.TextField(max_length=1000, help_text='Give a catchy description of your store', default= '')
    phone = models.CharField(max_length=20, default= "", null= False, blank= False)
    email = models.EmailField(default= '', max_length= 250, help_text= 'Your email name')
    location = models.CharField(help_text= 'Enter your store location', default= '', max_length= 250)

    def __str__(self):       
        return self.store_name
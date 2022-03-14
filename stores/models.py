from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
    	return self.category


@staticmethod
def get_all_categories():
    return Category.objects.all()


class Vendor(models.Model):
    #user = models.OneToOneField(UserProfile, related_name='vendor', on_delete=models.CASCADE)
    store_name = models.CharField(help_text= 'Your store name', default= '', max_length= 250)
    logo = models.ImageField( upload_to = 'staticfiles/profilepic')
    about = models.TextField(max_length=1000, help_text='Give a catchy description of your store', default= '')
    phone = models.CharField(max_length=20, default= "", null= False, blank= False)
    email = models.EmailField(default= '', max_length= 250, help_text= 'Your email name')
    location = models.CharField(help_text= 'Enter your store location', default= '', max_length= 250)

    def __str__(self):       
        return self.store_name

class Products(models.Model):
    product_tag = models.CharField(max_length=10, default= '')
    name = models.CharField(max_length=100, default = '')
    #store_name = models.ForeignKey(Vendor, default = '', on_delete= models.CASCADE)
    upload_Product_Image = models.ImageField(default='default.jpg', upload_to = 'staticfiles/products')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default = '')
    price = models.IntegerField()
    Size_Status = (
            ('X', 'Small'),
            ('XX', 'Large'),
            ('XXL', 'Extra large'),
            )

    size = models.CharField(max_length=5, choices= Size_Status, blank= True, default='X')
    stock = models.IntegerField()
    #imageUrl = models.URLField(default='')
    #created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products')
 
    def __str__(self):
        return self.product.product_Name


class Services(models.Model):
    service = models.ForeignKey(Vendor, default='', on_delete= models.CASCADE)
    service_name = models.CharField(max_length=250, default='', help_text= 'Describe your services ')
    service_description = models.TextField(max_length=1000, default='')
    payment = (
        ('pp', 'Pay per Hour'),
        ('p', 'Partition'),
        ('FR', 'Flat Rate'),
        )

    payment_method = models.CharField(max_length= 250, choices=payment, default='')
    
    def __str__(self):
        return self.service_name

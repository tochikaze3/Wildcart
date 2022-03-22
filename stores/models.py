from email.policy import default
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, default = None)
    slug = models.SlugField(default= '')

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Vendor(models.Model):
    #user = models.OneToOneField(UserProfile, related_name='vendor', on_delete=models.CASCADE)
    store_name = models.CharField(help_text= 'Your store name', default= '', max_length= 250)
    logo = models.ImageField( upload_to = 'profilepic')
    about = models.TextField(max_length=1000, help_text='Give a catchy description of your store', default= '')
    phone = models.CharField(max_length=20, default= "", null= False, blank= False)
    email = models.EmailField(default= '', max_length= 250, help_text= 'Your email name')
    location = models.CharField(help_text= 'Enter your store location', default= '', max_length= 250)

    def __str__(self):       
        return self.store_name

class Products(models.Model):
    product_name = models.CharField(max_length=100, default = '')
    #store_name = models.ForeignKey(Vendor, default = '', on_delete= models.CASCADE)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='')
    upload_Product_Image = models.ImageField(default='default.jpg', upload_to = 'products')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default = '')       
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)                                  
    price = models.DecimalField(max_digits=6, decimal_places=2)
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
        return self.product_name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://0.0.0.0:5000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://0.0.0.0:5000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://0.0.0.0:5000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.product_name)

        return thumbnail


class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'products')
 
    def __str__(self):
        return self.product.product_name



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

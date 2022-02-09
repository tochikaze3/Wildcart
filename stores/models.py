from django.db import models
from getnote import settings
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
        currency = models.CharField(max_length= 11, default= 00.00)
        price = models.DecimalField(max_digits=1000, decimal_places=2)
                
        
        def __str__(self):
            return self.product_Name

class ProductImage(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.product


class Vendor(models.Model):
    store_name = models.CharField(help_text= 'Your store name', default= '', max_length= 250)
    about = models.TextField(max_length=1000, help_text='Give a catchy description of your store', default= '')
    phone = models.CharField(max_length=20, default= "", null= False, blank= False)
    email = models.EmailField(default= '', max_length= 250, help_text= 'Your email name')
    location = models.CharField(help_text= 'Enter your store location', default= '', max_length= 250)

    def __str__(self):
        return self.store_name
============================================================================

class TweetFile(models.Model):
    tweep =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    media = models.FileField(upload_to='images')

    def __str__(self):
        return f"{self.tweep.username}'s media images"


class Tweets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    texts = models.TextField()
    file_content = models.ManyToManyField(TweetFile, related_name='file_content', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    tweep = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:

        verbose_name_plural = _('Tweets')

    def __str__(self):
        return f"{self.texts}"

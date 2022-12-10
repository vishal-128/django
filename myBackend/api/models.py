from django.db import models
#from api.category.models import Category
#from api.product.models import Product
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=350)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True,blank=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

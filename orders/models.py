from django.db import models
from datetime import datetime
from products.models import productlist

# Create your models here.
class orders_list(models.Model):
    product=models.OneToOneField(productlist,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.product.title
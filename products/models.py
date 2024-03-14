from django.db import models

# Create your models here.
class productlist(models.Model):
    title=models.CharField(max_length=200)
    usage=models.CharField(max_length=200)
    tag=models.CharField(max_length=250)
    price=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.title
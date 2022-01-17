from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.
class Item(models.Model):
    itemName=models.CharField(max_length=255)
    itemDesc=models.CharField(max_length=255)
    sellPrice=models.IntegerField(blank=False)
    quantity=models.IntegerField(blank=False)
    username=models.ForeignKey(User,on_delete=models.CASCADE,to_field='username')
    Category=models.CharField(max_length=255,default="null")

    def __str__(self):
        return self.itemName
class record(models.Model):
    itemId=models.IntegerField(blank=False)
    itemName=models.CharField(max_length=255)
    itemDesc=models.CharField(max_length=255)
    amount=models.IntegerField(blank=False)
    quantity=models.IntegerField(blank=False)
    username=models.ForeignKey(User,on_delete=models.CASCADE,to_field='username')
    customerName =models.CharField(max_length=255,default="null")
    phone=models.IntegerField(blank=False)
    

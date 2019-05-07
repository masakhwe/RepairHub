from django.db import models
from django.contrib.auth.models import User
# from .models import Category
#  from django.utils import timezone


class RepairRequest(models.Model):
    item_name = models.CharField('Item name', max_length=250)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #  image = models.ImageField()
    model_number = models.IntegerField('Model')
    request_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class Category(models.Model):
    name = models.CharField('category', max_length=250)

    def __str__(self):
        return self.name

from django.db import models


class Repairs(models.Model):
    customer_name = models.CharField('Customer Name', max_length=120)
    item_name = models.CharField('Item Name', max_length=60)
    serial_number = models.CharField('Serial Number', max_length=60)
    manufacturer = models.CharField('Manufacturer', max_length=50)
    photo = models.ImageField(upload_to='uploads/')
    fault_date = models.DateField(auto_now_add=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    fault_description = models.TextField()
    #  repair_status

    def __str__(self):
        return self.item_name


class Category(models.Model):
    office = models.CharField('Office ', max_length=50)
    kitchen = models.CharField('Kitchen Ware', max_length=50)
    entertainment = models.CharField('Entertainment', max_length=50)
    laundry = models.CharField('Laundry', max_length=50)

    def __str__(self):
        return self.office

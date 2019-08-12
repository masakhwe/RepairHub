from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Office')

    class Meta:
        ordering = ('name',)

    def __str__(self):

        return self.name


class Repairs(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField('Device Name', max_length=60,
                                   default='device')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    serial_number = models.CharField('Serial Number', max_length=60)
    manufacturer = models.CharField('Manufacturer', max_length=50)
    description = models.TextField('Fault Description', max_length=100)
    photo = models.ImageField(upload_to='repair_pics', default='default.png')

    fault_date = models.DateField(auto_now_add=True)
    date_reported = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)
        # To resize the uploaded image if its too large
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        return self.device_name

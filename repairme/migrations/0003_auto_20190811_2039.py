# Generated by Django 2.2.3 on 2019-08-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairme', '0002_auto_20190807_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairs',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='repair_pics'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-07-13 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairme', '0002_auto_20190713_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairs',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

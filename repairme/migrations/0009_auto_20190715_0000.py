# Generated by Django 2.2.2 on 2019-07-14 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairme', '0008_auto_20190714_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairs',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairme.Category'),
        ),
        migrations.AlterField(
            model_name='repairs',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

from __future__ import unicode_literals

from django.db import models

class Product(models.Model):

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, help_text='Enter product title')
    price = models.FloatField(help_text='Enter product price')

    def __str__(self):
        return self.title


class Cart(models.Model):

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, help_text='Enter Cart title')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title
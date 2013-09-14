from django.db import models
from django.db.models.signals import pre_save

class Product(models.Model):

    CATEGORY1 = (
        (0, 'Aaa'),
        (1, 'Bbb'),
    )

    CATEGORY2 = (
        (0, 'Ccc'),
        (1, 'Ddd'),
    )

    CATEGORY3 = (
        (0, 'Eee'),
        (1, 'Fff'),
    )

    name = models.CharField(max_length=255, null=False)
    price = models.PositiveIntegerField(null=False)

    price_range = models.PositiveSmallIntegerField(blank=True, null=True)

    category1 = models.PositiveSmallIntegerField(choices=CATEGORY1, default=0)
    category2 = models.PositiveSmallIntegerField(choices=CATEGORY2, default=0)
    category3 = models.PositiveSmallIntegerField(choices=CATEGORY3, default=0)

    check1 = models.BooleanField(default=False)
    check2 = models.BooleanField(default=False)
    check3 = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def update_price_range(sender, instance, **kwargs):
    price = instance.price
    if 0 <= price <= 5000:
        instance.price_range = 0
    elif 5000 < price <= 10000:
        instance.price_range = 1
    elif 10000 < price <= 20000:
        instance.price_range = 2
    elif 20000 < price <= 30000:
        instance.price_range = 3
    elif 30000 < price <= 50000:
        instance.price_range = 4
    else:
        instance.price_range = 5
pre_save.connect(update_price_range, sender=Product)

class ProductStat(models.Model):
    product = models.OneToOneField('Product', primary_key=True)
    liked = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

class ProductStock(models.Model):
    product = models.OneToOneField('Product', primary_key=True)
    number = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

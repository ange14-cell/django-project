from time import timezone
from django.db import models
from django.utils.text import slugify
from ktcb.settings import AUTH_USER_MODEL


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='product', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.stock})"

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)

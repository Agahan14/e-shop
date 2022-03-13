from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from products.models import Product

class CartItem(models.Model):

    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=10)

    def __str__(self):
        return f"{self.id} {self.products}"


class Cart(models.Model):

    total_price = models.FloatField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_order = models.BooleanField(default=False)
    products = GenericRelation(CartItem, object_id_field="cart", content_type_field="content_type")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="cart_user", on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.id} {self.user}"


class Order(models.Model):

    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="order_user", on_delete=models.CASCADE,)
    cart = models.ForeignKey(Cart, related_name="order_cart", on_delete=models.CASCADE)
    products = GenericRelation(CartItem, object_id_field="cart", content_type_field="content_type")

    def __str__(self):
        return f"{self.id} {self.user}"

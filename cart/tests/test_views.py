from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from ..models import (
    Cart,
    CartItem
)


class ProductTest(APITestCase):
    def setUp(self) -> None:
        self.cart = Cart.objects.create(is_order=False)
        self.cartitem = CartItem.objects.create(quantity=2, price=123)

    def test_cart_get(self):
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_carts_detail(self):
        response = self.client.get(reverse("carts", kwargs={'id': self.cart.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_item_category_get(self):
        response = self.client.get(reverse("cart-item"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cart_items_detail(self):
        response = self.client.get(reverse("cart-items", kwargs={'id': self.cartitem.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

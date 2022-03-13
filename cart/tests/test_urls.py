from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import (
    CartView,
    CartDetailView,
    CartItemView,
    CartItemDetailView,
    OrderView,
    OrderDetailView
)


class TestUrls(SimpleTestCase):

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, CartView)

    def test_carts_url_is_resolved(self):
        url = reverse('carts')
        self.assertEquals(resolve(url).func.view_class, CartDetailView)

    def test_cart_item_url_is_resolved(self):
        url = reverse('cart-item')
        self.assertEquals(resolve(url).func.view_class, CartItemView)

    def test_cart_items_url_is_resolved(self):
        url = reverse('cart-items')
        self.assertEquals(resolve(url).func.view_class, CartItemDetailView)

    def test_order_url_is_resolved(self):
        url = reverse('order')
        self.assertEquals(resolve(url).func.view_class, OrderView)

    def test_orders_url_is_resolved(self):
        url = reverse('orders')
        self.assertEquals(resolve(url).func.view_class, OrderDetailView)
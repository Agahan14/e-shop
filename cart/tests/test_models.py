from django.test import TestCase

from ..models import Cart, Order, CartItem
from users.models import User


class CartModelsTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name="user",
            email="user@user.com",
            role="Customer/Admin"
        )
        self.cart = Cart.objects.create(pk=1, user=self.user)
        self.order = Order.objects.create(user=self.user, cart=self.cart)
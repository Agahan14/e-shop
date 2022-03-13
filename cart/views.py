from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CartSerializer, CartItemSerializer, OrderSerializer
from .models import Cart, CartItem, Order
from .permissions import OwnerPermission


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Cart.objects.all()


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = (OwnerPermission,)
    queryset = Cart.objects.all()


class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
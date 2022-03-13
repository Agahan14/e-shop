from rest_framework import serializers

from .models import Cart, CartItem, Order


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        exclude = ['content_type']


class CartSerializer(serializers.ModelSerializer):

    products = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'total_price',
            'created_date',
            'is_order',
            'products'
        ]

    def get_total_price(self, obj):
        total_price = 0
        for product in obj.products.all():
            total_price += product.price * product.quantity

        return total_price


class OrderSerializer(serializers.Serializer):

    products = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'cart',
            'order_date',
            'total_price',
            'products']

    def get_total_price(self, obj):
        total_price = 0
        for product in obj.products.all():
            if product.discount > 0:
                total_price += (product.price - (product.price
                                                 * (product.discount/100))) * product.quantity
            else:
                total_price += product.price * product.quantity

        return total_price
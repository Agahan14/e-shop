from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from ..models import (
    ProductCategory,
    Product,
    Comment
)


class ProductTest(APITestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(title='milk',
                                          description='milky',
                                          pictures=None,
                                          price=12345,
                                          discount=123
                                          )
        self.category = ProductCategory.objects.create(name='milky')
        self.comment = Comment.objects.create(rate=1,
                                         content='Not good',
                                         replies=None

    def test_product_get(self):
        response = self.client.get(reverse("product"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        response = self.client.get(reverse("products", kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_category_get(self):
        response = self.client.get(reverse("product-category"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_category_detail(self):
        response = self.client.get(reverse("product-categories", kwargs={'id': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_get(self):
        response = self.client.get(reverse("comment"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_detail(self):
        response = self.client.get(reverse("comments", kwargs={'id': self.comment.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

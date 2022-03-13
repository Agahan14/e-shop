from django.test import TestCase

from ..models import ProductCategory, Product, Comment
from users.models import User


class ProdcutCategoryTest(TestCase):
    def setup(self):
        self.productcategory = ProductCategory.objects.create(name='books')

    def test_title_max_length(self):
        max_length = self.productcategory._meta.get_field("title").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_title(self):
        expected_category_name = self.productcategory.name
        self.assertEquals(expected_category_name, str(self.productcategory))


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(
            title="books1"
        )
        self.user = User.objects.create(username="user", email="user@mail.ru",password="123456")
        self.product = Product.objects.create(
            title="Book",
            description="Interesting",
            price=12345,
            category=ProductCategory.objects.get(id=self.category.id),
            user=User.objects.get(id=self.user.id),
        )

    def test_product_name_is_title(self):
        expected_product_name = self.product.title
        self.assertEquals(expected_product_name, str(self.product))


class OrderModelTest(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(
            title="books1"
        )
        self.user = User.objects.create(username="user", email="user@mail.ru",password="123456")
        self.product = Product.objects.create(
            title="Book",
            description="Interesting",
            price=12345,
            category=ProductCategory.objects.get(id=self.category.id),
            user=User.objects.get(id=self.user.id),
        )
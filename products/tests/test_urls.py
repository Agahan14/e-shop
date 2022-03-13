from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import (
    ProductView,
    ProductDetailView,
    ProductCategoryView,
    ProductCategoryDetailView,
    CommentView,
    CommentDetailView
)


class TestUrls(SimpleTestCase):

    def test_product_url_is_resolved(self):
        url = reverse('product')
        self.assertEquals(resolve(url).func.view_class, ProductView)

    def test_products_url_is_resolved(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_product_category_url_is_resolved(self):
        url = reverse('product-category')
        self.assertEquals(resolve(url).func.view_class, ProductCategoryView)

    def test_product_categories_url_is_resolved(self):
        url = reverse('product-categories')
        self.assertEquals(resolve(url).func.view_class, ProductCategoryDetailView)

    def test_commet_url_is_resolved(self):
        url = reverse('comment')
        self.assertEquals(resolve(url).func.view_class, CommentView)

    def test_coments_url_is_resolved(self):
        url = reverse('comments')
        self.assertEquals(resolve(url).func.view_class, CommentDetailView)
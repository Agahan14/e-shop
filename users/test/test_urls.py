from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import (
    RegisterAPIView,
    LoginAPIView,
    UserAPIView,
    RefreshAPIView,
    LogoutAPIView
)


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterAPIView)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginAPIView)

    def test_user_category_url_is_resolved(self):
        url = reverse('user')
        self.assertEquals(resolve(url).func.view_class, UserAPIView)

    def test_refresh_categories_url_is_resolved(self):
        url = reverse('refresh')
        self.assertEquals(resolve(url).func.view_class, RefreshAPIView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutAPIView)

    def test_coments_url_is_resolved(self):
        url = reverse('comments')
        self.assertEquals(resolve(url).func.view_class, CommentDetailView)
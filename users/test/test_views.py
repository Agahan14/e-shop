from django.test import TestCase

from ..models import User


class TestCreating(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name="user1",
            email="user1@admin.com",
            password="user123",
            role="admin",
            first_name="Angel",
            last_name="Demon",
            address="address",
            phone="phone",
        )
        self.invalid_payload = {
            "username": "",
            "email": "user@user.com",
            "password": "user123",
        }

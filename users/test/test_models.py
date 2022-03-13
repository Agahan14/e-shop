from django.test import TestCase

from ..models import User


class ModelsTests(TestCase):

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

    def test_create_user_without_required_fields(self):
        """Test create user without required fields"""

        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="user@admin.com", password="user123", username=None
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="user@admin.com", password=None, username="user"
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email=None, password="user123", username="user"
            )
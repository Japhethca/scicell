from django.test import TestCase
from apps.core.models import User
from django.core.exceptions import ValidationError


# User test cases
class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test.user@domain.com",
            password="test12345"
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, 'test.user@domain.com')

    def test_does_not_create_user_with_invalid_email(self):
        with self.assertRaises(ValidationError):
            User.objects.create_user(
                email='invalidemal',
                password="invalid1234"
            )

    def test_create_admin_user(self):
        admin = User.objects.create_superuser(
            email="admin@mail.com",
            password="admin12345"
        )
        self.assertEqual(admin.email, 'admin@mail.com')

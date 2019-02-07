from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = 'test@onet.pl'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if email for a new user is normalizes"""
        email = 'test@INTERIA.PL'
        user = get_user_model().objects.create_user(email=email, password='test123')

        self.assertEqual(user.email, email.lower())

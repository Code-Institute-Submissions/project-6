from django.test import TestCase
from .models import User


class TestUserModel(TestCase):

    def test_user_model(self):
        item = User(name="Test", email="test@test.com", phone="03676545676")
        item.save()		
        self.assertEqual(item.name, "Test")
        self.assertEqual(item.email, "test@test.com")
        self.assertEqual(item.img, "")
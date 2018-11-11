from django.test import TestCase
from .models import User, UserProfile


class TestUserModel(TestCase):

    def test_user_model(self):
        item = User(username="Test", email="test@test.com")
        item.save()		
        self.assertEqual(item.username, "Test")
        self.assertEqual(item.email, "test@test.com")

class TestUserProfile(TestCase):

    def test_user_profile_model(self):
        user = User(username="Test", email="test@test.com")
        user.save()
        profile = UserProfile(user=user, phone="123456")
        profile.save()

        self.assertEqual(profile.user, user)
        self.assertEqual(profile.phone, "123456")

from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from .models import Listing


class TestListingModel(TestCase):

    def test_listing_model(self):

        user = User(username="Test", email="test@test.com")
        user.save()

        item = Listing(
            title="Test",
            address="address",
            city="city",
            state="state",
            zipcode="123456",
            price=100000000,
            bedrooms=5,
            bathrooms=2,
            garage=1,
            square_feet=450,
            seller=user)
        item.save()
        self.assertEqual(item.title, "Test")
        self.assertEqual(item.address, "address")
        self.assertEqual(item.state, "state")
        self.assertEqual(item.zipcode, "123456")

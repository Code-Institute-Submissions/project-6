from django.test import TestCase
from .models import Listing


class TestListingModel(TestCase):

    def test_listing_model(self):
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
			square_feet=450)
        item.save()		
        self.assertEqual(item.title, "Test")
        self.assertEqual(item.address, "address")
        self.assertEqual(item.state, "state")
        self.assertEqual(item.zipcode, "123456")
		
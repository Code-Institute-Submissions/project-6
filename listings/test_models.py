from django.test import TestCase
from fake_data_gen.testing_models import TestingData  
from listings.models import Listing

class TestListingModel(TestCase):

    def test_listing_model(self):

        TestingData()
        item = Listing.objects.get(pk=1)
        self.assertEqual(item.title, "Test")
        self.assertEqual(item.address, "address")
        self.assertEqual(item.state, "state")
        self.assertEqual(item.zipcode, "123456")

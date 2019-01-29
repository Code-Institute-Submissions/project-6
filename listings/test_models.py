from django.test import TestCase
from django.db import IntegrityError
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

    def test_for_duplicated_zipcode(self):
        TestingData(zipcode="MK45 76HK")

        with self.assertRaises(IntegrityError):
            TestingData(zipcode="MK45 76HK")

    def test_for_duplicated_zipcode_lower(self):
        TestingData(zipcode="MK45 76HK")

        with self.assertRaises(IntegrityError):
            TestingData(zipcode="mk45 76hk")

    def test_for_duplicated_zipcode_white_spaces(self):
        TestingData(zipcode="MK45 76HK")

        with self.assertRaises(IntegrityError):
            TestingData(zipcode="  mk45   76hk  ")

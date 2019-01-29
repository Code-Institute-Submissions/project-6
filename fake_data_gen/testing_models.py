from django.contrib import auth
from django.test import TestCase, Client
from accounts.models import User, UserProfile
from listings.models import Listing


class TestingData(TestCase):

    def __init__(self, zipcode="123456"):
        self.user = self.create_user()
        self.user_profile = self.create_profile()
        self.zipcode = zipcode
        self.listing = self.create_listing()        

    def create_user(self):
        new_user = User(username="Test", email="test@test.com")
        new_user.set_password('123456')
        new_user.save()
        return new_user

    def create_profile(self):
        new_profile = UserProfile(user=self.user, phone="123456789")
        new_profile.save()
        return new_profile

    def create_listing(self):
        new_listing = Listing(title="Test",
                              address="address",
                              city="city",
                              state="state",
                              zipcode=self.zipcode,
                              main_img="/media/test.jpg",
                              price=100000000,
                              bedrooms=5,
                              bathrooms=2,
                              garage=1,
                              square_feet=450,
                              seller=self.user)
        new_listing.save()
        return new_listing

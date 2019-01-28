from django.contrib.auth.models import User
from django.test import TestCase, Client
from fake_data_gen.testing_models import TestingData


class TestViews(TestCase):
    def test_get_all_listings(self):
        page = self.client.get("/listings/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "houses.html")

    def test_get_single_listing(self):
        TestingData()
        page = self.client.get("/listings/house/1")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "house.html")

    def test_get_search(self):
        page = self.client.get("/listings/search")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "search.html")

    def test_redirect_nonauth_user_from_add_house_page(self):
        page = self.client.get("/listings/house/add_house/1")
        self.assertEqual(page.status_code, 302)

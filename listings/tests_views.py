from django.test import TestCase

class TestViews(TestCase):

	def test_get_all_listings(self):
		page = self.client.get("/listings/")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "plants.html")

	""" def test_get_single_listing(self):
		page = self.client.get("123456")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "plant.html") """

	def test_get_search(self):
		page = self.client.get("/listings/search")
		self.assertEqual(page.status_code, 200)
		self.assertTemplateUsed(page, "search.html")

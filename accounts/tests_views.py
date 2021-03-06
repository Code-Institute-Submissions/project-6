from django.test import TestCase
from fake_data_gen.testing_models import TestingData


class TestViews(TestCase):
    def test_get_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")

    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_redirect_nonauth_user_from_profile_page(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 302)

from django.test import TestCase


class HomeViewTest(TestCase):
    def test_returns_200(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_site_name_in_context(self) -> None:
        response = self.client.get("/")
        self.assertIn("site_name", response.context)

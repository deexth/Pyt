from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomeView

# Create your tests here.


class HomepageTests(SimpleTestCase):
    """ "Testing the status code of the homepage"""

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_by_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_html(self):
        self.assertContains(self.response, "Welcome to our Chatbot")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homeview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)
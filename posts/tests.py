from django.test import SimpleTestCase
from django.urls import reverse

from .models import Post


class ModelTest(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        cls.post = Post.objects.create(text="another boring test")

    def test_model(self):
        self.assertEqual(self.post.text, "another boring test")

    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "another boring test")

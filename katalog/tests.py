from pydoc import resolve
from django.test import TestCase
from django.urls import reverse

from katalog.models import CatalogItem
from katalog.views import show_katalog

# Create your tests here.
class KatalogTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name_html(self):  
        response = self.client.get(reverse('katalog:show_katalog'))
        self.assertEqual(response.status_code, 200)

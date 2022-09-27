from pydoc import resolve
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from mywatchlist.models import MyWatchListItem
from mywatchlist.views import show_film, show_json, show_xml, show_json_by_id

# Create your tests here.


class mywatchlistTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("show_film"))
        self.assertEqual(response.status_code, 200)
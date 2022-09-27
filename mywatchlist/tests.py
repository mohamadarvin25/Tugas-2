from pydoc import resolve
from django.test import TestCase
from django.urls import reverse

from mywatchlist.models import MyWatchListItem
from mywatchlist.views import show_film, show_json, show_xml, show_json_by_id

# Create your tests here.


class MyWatchlistTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    
    def test_url_available_by_name_html(self):  
        response = self.client.get(reverse('mywatchlist:show_film'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name_xml(self):  
        response = self.client.get(reverse('mywatchlist:show_xml'))
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name_json(self):  
        response = self.client.get(reverse('mywatchlist:show_json'))
        self.assertEqual(response.status_code, 200)
from django.urls import path
# now import the views.py file into this code
from mywatchlist.views import show_film,show_xml,show_json,show_json_by_id

app_name = 'mywatchlistt'
urlpatterns = [
    path('', show_film, name='show_film'),
    path('html/', show_film, name='show_film'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]

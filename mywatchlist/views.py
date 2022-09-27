from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
from mywatchlist.models import MyWatchListItem

def show_film(request):
    return render(request, "mywatchlist.html",context)

data_mywatchlist_item = MyWatchListItem.objects.all()
context = {
    'list_film': data_mywatchlist_item,
    'nama' : 'Mohamad Arvin Fadriasnyah',
    'id'   : '2006596996'
}

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_mywatchlist_item), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_mywatchlist_item), content_type="application/json")

data = MyWatchListItem.objects.filter(pk=1)

def show_json_by_id(request,id):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
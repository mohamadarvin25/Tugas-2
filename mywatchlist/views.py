from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
from mywatchlist.models import MyWatchListItem


def show_film(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    context = {
        'list_film': data_mywatchlist_item,
        'nama': 'Mohamad Arvin Fadriasnyah',
        'id': '2006596996'
    }
    return render(request, "mywatchlist.html", context)


def show_xml(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist_item), content_type="application/xml")


def show_json(request):
    data_mywatchlist_item = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist_item), content_type="application/json")





def show_json_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=1)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

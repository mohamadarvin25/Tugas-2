from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.


def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_catalog_item,
        'nama': 'Mohamad Arvin Fadriasnyah',
        'id': '2006596996'
    }
    return render(request, "katalog.html", context)

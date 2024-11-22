from django.shortcuts import render
from .models import PageRequest

def page_request_list(request):
    items = PageRequest.objects.all()  # Fetch all items
    return render(request, 'printable_pages.html', {'items': items})

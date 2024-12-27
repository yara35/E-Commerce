from django.shortcuts import render

from item.models import category, item


def index(request):
    items = item.objects.filter(is_sold = False)[0:6]
    categories = category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request, 'core/contact.html')
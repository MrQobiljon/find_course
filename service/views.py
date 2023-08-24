from django.db.models import Q
from django.shortcuts import render
from .models import Category, WebService, Source

# Create your views here.


def index(request):
    categories = Category.objects.all()
    web_services = WebService.objects.all()
    sources = Source.objects.all()
    context = {
        'categories': categories,
        'web_services': web_services,
        'sources': sources
    }
    return render(request, 'service/index.html', context)


def test(request):

    categories = Category.objects.all()
    sorters_by_cat = []
    for category in categories:
        cat = request.GET.get(str(category.slug))
        if cat:
            sorters_by_cat.append(cat)
            print(sorters_by_cat, '-----------------------------------------')

    web_services = WebService.objects.all()
    sorters_by_ser = []
    for web_service in web_services:
        ser = request.GET.get(str(web_service.slug))
        if ser:
            sorters_by_ser.append(ser)
            print(sorters_by_ser, '-----------------------------------------')

    if sorters_by_cat and sorters_by_ser or not sorters_by_cat and not sorters_by_ser:
        sources = Source.objects.filter(category__name__in=sorters_by_cat, web_service__name__in=sorters_by_ser)
    elif sorters_by_cat:
        sources = Source.objects.filter(category__name__in=sorters_by_cat)
    elif sorters_by_ser:
        sources = Source.objects.filter(web_service__name__in=sorters_by_ser)

    context = {
        'categories': categories,
        'web_services': web_services,
        'sources': sources
    }

    return render(request, 'service/index.html', context)


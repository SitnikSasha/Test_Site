from django.shortcuts import render, get_object_or_404
from .models import CategoryItem, Item

# Create your views here.


def index(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/index.html', data)


def about(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/about.html', data)


def urgent_repairs(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/urgent_repairs.html', data)


def d_dev(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/3D_dev.html', data)


def exchange_fund(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/exchange_fund.html', data)


def restoration(request):
    category = CategoryItem.objects.all()
    data = {
        'category': category
    }
    return render(request, 'main/restoration.html', data)


def show_category(request, category_slug):
    items = Item.objects.all()
    category = CategoryItem.objects.all()
    data = {
        'items': items,
        'category': category,
        'cat': category_slug,
    }
    return render(request, 'main/portfolio-overview.html', data)

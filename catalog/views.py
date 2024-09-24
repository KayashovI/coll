from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def index(request: HttpRequest) -> HttpResponse:
    products = models.Product.objects.all()
    context = {'products': products}

    return render(request, 'catalog/index.html', context)


def product(request: HttpRequest, product_id:int) -> HttpResponse:
    product = models.Product.objects.get(pk=product_id)
    context = {'product':product}

    return render(request, 'catalog/product.html', context)
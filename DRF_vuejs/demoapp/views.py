from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('product-list', request=request, format=format),
        'carts': reverse('cart-list', request=request, format=format)
    })


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


def page_render(request):

    return render_to_response('index.html')


def products_list(request):

    context = {}
    context['products'] = Product.objects.all()

    html = TemplateResponse(request, 'adding_to_cart.html', context)
    return HttpResponse(html.render())
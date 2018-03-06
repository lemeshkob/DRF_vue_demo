from django.conf.urls import url
from .views import ProductViewSet, CartViewSet, api_root, page_render, products_list
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt


product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
cart_list = CartViewSet.as_view({
    'get': 'create'
})
cart_detail = CartViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^$', csrf_exempt(page_render)),
    url(r'^products/$', csrf_exempt(product_list), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', csrf_exempt(product_detail), name='product-detail'),
    url(r'^carts/$',  products_list, name='cart-list'),
    url(r'^carts/(?P<pk>[0-9]+)/$', csrf_exempt(cart_detail), name='cart-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

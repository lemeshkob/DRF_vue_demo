from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from demoapp import views
import demoapp
from demoapp import urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'carts', views.CartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(demoapp.urls)),
    path('api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

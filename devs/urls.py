from django.urls import path
from .views import HelloWorld
from rest_framework.routers import DefaultRouter
from .api.views import DevApiView, DevViewSet, DevModelViewSet

router_dev = DefaultRouter()

# router_dev.register(prefix='devs', basename='devs', viewset=DevViewSet)
router_dev.register(prefix='devs', basename='devs', viewset=DevModelViewSet)


urls = [
    # path('', HelloWorld.as_view())
    # path('',  DevApiView.as_view())
]

urlpatterns = urls + router_dev.get_urls()
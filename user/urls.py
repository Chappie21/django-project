from rest_framework.routers import DefaultRouter
from .api.views import UserModelViewSet
from .api.ApiView import UserApiViewListPost, UserApiViewGetUpdatedDelete
from django.urls import path

# view sets routers
user_router = DefaultRouter()
user_router.register(prefix='user', basename='user', viewset=UserModelViewSet)

# api view routers
urls = [
    path(route='users/apiview/', view=UserApiViewListPost.as_view()),
    path(route='users/apiview/<int:pk>/', view=UserApiViewGetUpdatedDelete.as_view())
]

urlpatterns = urls + user_router.get_urls()
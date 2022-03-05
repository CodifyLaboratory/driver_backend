from rest_framework import routers
from useful.api.view_viewset import UsefulViewset

useful_router = routers.DefaultRouter()
useful_router.register('useful', UsefulViewset, basename='Useful')

from rest_framework import routers
from common_base.api.views import CommonBaseViewSet

base_router = routers.DefaultRouter()
base_router.register('base', CommonBaseViewSet, basename='Common Base')
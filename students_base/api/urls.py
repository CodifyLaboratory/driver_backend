from rest_framework import routers
from students_base.api.views import LessonView

base_router = routers.DefaultRouter()
base_router.register('base',LessonView, basename='Students base')
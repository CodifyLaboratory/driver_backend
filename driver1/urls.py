from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from news.api.urls import news_router
from driver1.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from useful.api.urls import useful_router
from comments.api.urls import comments_router
from common_base.api.urls import base_router
from feedback.api.urls import feedback_router

from . import settings

router = routers.DefaultRouter()
router.registry.extend(news_router.registry)
router.registry.extend(useful_router.registry)
router.registry.extend(comments_router.registry)
router.registry.extend(base_router.registry)
router.registry.extend(feedback_router.registry)

urlpatterns = [
    path('driver_admin/', admin.site.urls),
#path to djoser endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
#path to our account's app endpoint
    path('about_user/', include('about_user.urls')),
    path('test/', include('test.urls', namespace='test')),
    path('exam/', include('exam.urls', namespace='exam')),
    path('api/', include(router.urls), name='api'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Driver API",
        default_version='v1',
        url='localhost:8000',
        description="Driver api",
        terms_of_service="",
        contact=openapi.Contact(email="www.qwerty19881509@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = urlpatterns + [
    path(r'api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=5), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc',
         cache_timeout=5), name='schema-redoc-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from .views import AboutUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"about_user", AboutUserViewSet, basename='about_user')
urlpatterns = router.urls

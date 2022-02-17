from django.urls import path
from .views import UserRegisterAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="user-registration"),
    path('login/', obtain_auth_token, name='user-obtain_auth_token'),
]

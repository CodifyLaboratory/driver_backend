from rest_framework import views, response, status
from rest_framework.permissions import AllowAny
from .serializer import MyUserSerializer


class UserRegisterAPIView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

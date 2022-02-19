# from rest_framework import viewsets, response, status
# from .serializers import MyUserSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
#
#
# class MyUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = MyUserSerializer
#
#
# class MyUserList(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]
#
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

# class UserProfileListCreateView(ListCreateAPIView):
#     queryset = userProfile.objects.all()
#     serializer_class = userProfileSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)
#
#
# class userProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = userProfile.objects.all()
#     serializer_class = userProfileSerializer
#     permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


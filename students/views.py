from django.shortcuts import render
from .models import Student
from rest_framework import viewsets, views, status, parsers, response, serializers
from .serializer import StudentSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse


class StudentListAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise serializers.ValidationError(detail="obj does not exist")
        return student

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(instance=student)
        return JsonResponse(data=serializer.data, status=200)

    def patch(self, request, pk):
        student = self.get_object(pk=pk)
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializer(instance=student, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = self.get_object(pk=pk)
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

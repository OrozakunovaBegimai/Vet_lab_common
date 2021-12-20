

from django.http import HttpResponse
from rest_framework import viewsets, response, views
from django.shortcuts import get_object_or_404

from .models import Employee, EmployeeServices, EmployeeComment
from .serializers import EmployeeSerializers, EmployeeServicesSerializer, EmployeeCommentSerializer, EmployeeListSerializers


class EmployeesListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        students = Employee.objects.all()
        serializer = EmployeeListSerializers(instance=students, many=True)
        return response.Response(data=serializer.data, status=200)


class EmployeeDetailAPIView(views.APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            return HttpResponse(status=404)
        serializer = EmployeeSerializers(instance=employee)
        return response.Response(data=serializer.data, status=200)


class EmployeeCommentDetailAPIView(views.APIView):
    def get_object(self, comment_pk):
        try:
            comment = EmployeeComment.objects.get(id=comment_pk)
        except EmployeeComment.DoesNotExist:
            return HttpResponse(status=404)
        return comment

    def get(self, request, comment_pk, *args, **kwargs):
        comment = self.get_object(comment_pk)
        serializer = EmployeeCommentSerializer(instance=comment)
        return response.Response(data=serializer.data, status=200)

    def put(self, request, comment_pk, *args, **kwargs):
        comment = self.get_object(comment_pk)
        serializer = EmployeeCommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.data, status=400)

    def delete(self, request, comment_pk, *args, **kwargs):
        comment = self.get_object(comment_pk)
        comment.delete()
        return HttpResponse(status=204)
from .models import Employee, EmployeeServices, EmployeeComment
from rest_framework import serializers


# some views

class EmployeeServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeServices
        fields = ['id', 'name', 'employee']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response['name']


class EmployeeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeComment
        fields = ['id', 'content', 'employee', 'author', 'grade', 'date_of_comment']


class EmployeeSerializers(serializers.ModelSerializer):
    employee_services = EmployeeServicesSerializer(many=True, read_only=True)
    employee_comments = EmployeeCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'experience', 'city_of_work', 'image', 'employee_services',
                  'employee_comments']


class EmployeeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'experience', 'city_of_work', 'image']



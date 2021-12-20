from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    city_of_work = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


class EmployeeServices(models.Model):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_services')

    def __str__(self):
        return self.name


class EmployeeComment(models.Model):
    content = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_of_comment = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee}-{self.author}'


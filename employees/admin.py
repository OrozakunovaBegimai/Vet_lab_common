from django.contrib import admin

from .models import Employee, EmployeeServices, EmployeeComment

admin.site.register(Employee)
admin.site.register(EmployeeServices)
admin.site.register(EmployeeComment)

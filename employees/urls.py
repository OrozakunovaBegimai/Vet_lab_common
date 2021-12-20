from django.urls import path
from .views import EmployeesListAPIView, EmployeeDetailAPIView, EmployeeCommentDetailAPIView

urlpatterns =[
    path('employees/', EmployeesListAPIView.as_view(), name='employees-list'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employee_comments/<int:comment_pk>/', EmployeeCommentDetailAPIView.as_view(), name='employee_comments-detail'),
]
from django.urls import path
from course.api import views

urlpatterns = [
    path('v1/branches/',  views.BranchAPIView.as_view(), name='branches'),
    path('v1/branches/<int:pk>/', views.BranchDetailAPIView.as_view(), name='branch_detail'),
    path('v1/groups/', views.GroupAPIView.as_view(), name='groups'),
    path('v1/groups/<int:pk>/', views.GroupDetailAPIView.as_view(), name='group_detail'),
    path('v1/students/', views.StudentAPIView.as_view(), name='students'),
    path('v1/students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student_detail'),
]
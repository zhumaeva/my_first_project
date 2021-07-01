#from django.urls.conf import include
#from course.serializers import StudentSerializer
#import random
from django.urls import path, include
from course import views
urlpatterns = [
    path('', views.my_main_page, name='my_main_page'),
    path('branches/', views.BranchListView.as_view(), name='branches_list'),
    path('branches/<int:branch_id>/', views.BranchDetailView.as_view(), name='branch_detail'),
    path('branches/create/', views.BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:branch_id>/edit/', views.BranchUpdateView.as_view(), name='branch_edit'),
    path('branches/<int:branch_id>/delete/', views.BranchDeleteView.as_view(), name='branch_delete'),
    path('branches/random', views.branch_random, name = "branch_random"),
    
    
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/<int:group_id>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/',views.GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:group_id>/edit/', views.GroupUpdateView.as_view(), name='group_edit'),
    path('group/<int:group_id>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('groups/random', views.group_random, name = "group_random"),

    
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:student_id>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:student_id>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('student/random', views.student_random, name = "student_random"),
    path('api/', include('course.api.urls'))
]

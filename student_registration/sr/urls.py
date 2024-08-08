from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_course/', views.add_course, name='add_course'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
]

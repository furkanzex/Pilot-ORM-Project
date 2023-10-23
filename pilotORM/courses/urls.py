from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.create_course, name='courses'),
    path('students/', views.create_student, name='students'),
    path('takenCourses/', views.create_taken_course, name='takenCourses'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_course/', views.create_course, name='create_course'),
    path('course_list/', views.course_list, name='course_list'),
    path('create_taken_course/', views.create_taken_course, name='create_taken_course'),
    path('student_list/', views.student_list, name='student_list'),
]
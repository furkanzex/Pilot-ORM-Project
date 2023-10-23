from django import forms
from .models import Student, Course, TakenCourse

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_number']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'duration']

class TakenCourseForm(forms.ModelForm):
    class Meta:
        model = TakenCourse
        fields = ['student', 'course', 'week_day', 'start_time']

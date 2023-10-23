from django.shortcuts import render, redirect

from courses.models import Student, Course, TakenCourse
from .forms import StudentForm, CourseForm, TakenCourseForm

def home(request):
    context = {
        'page_title': 'Ana Sayfa Başlığı',
        'welcome_message': 'PilotORM',
    }
    return render(request, 'courses/templates.html', context)


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

def takenCourses(request):
    takenCourses = TakenCourse.objects.all()
    return render(request, 'courses/takenCourses.html', {'takenCourses': takenCourses})

def create_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save() 
            return render(request, 'courses/students.html', {'student_form': student_form})
    else:
        student_form = StudentForm()
    
    return render(request, 'courses/students.html', {'student_form': student_form})

def create_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save() 
            return render(request, 'courses/courses.html', {'course_form': course_form})
    else:
        course_form = CourseForm()

    return render(request, 'courses/courses.html', {'course_form': course_form})

def create_taken_course(request):
    if request.method == 'POST':
        taken_course_form = TakenCourseForm(request.POST)
        if taken_course_form.is_valid():
            taken_course_form.save() 
            return render(request, 'courses/takenCourses.html', {'taken_course_form': taken_course_form})
    else:
        taken_course_form = TakenCourseForm()

    return render(request, 'courses/takenCourses.html', {'taken_course_form': taken_course_form})

def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'courses/stdList.html', context)

def course_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/crsList.html', context)
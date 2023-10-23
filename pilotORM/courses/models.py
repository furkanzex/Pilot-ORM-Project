from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.student_number}"

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name

class TakenCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=20)
    start_time = models.TimeField()

    def __str__(self):
        return f"{self.student.first_name} - {self.course.course_name}"
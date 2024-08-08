from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm


def home(request):
    return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

from django import forms
from .models import Student, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', ]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email', 'number', 'age', 'enrollment_date', 'course']

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

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(name__in=['Python', 'PHP', 'Java'])
        self.fields['course'].queryset = Course.objects.filter(name__iexact='Python') | \
                                  Course.objects.filter(name__iexact='PHP') | \
                                  Course.objects.filter(name__iexact='Java')


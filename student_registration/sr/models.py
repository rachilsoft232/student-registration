from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    number = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    enrollment_date = models.DateField()
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

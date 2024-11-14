from django.db import models
# authentiation/models.py
from django.contrib.auth.models import AbstractUser

# Custom User model to distinguish between students and teachers
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add student-specific fields here, e.g., grade, enrollment date, etc.
    grade = models.CharField(max_length=20)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.user.username

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add teacher-specific fields here, e.g., department, hire date, etc.
    department = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.user.username

# Create your models here.

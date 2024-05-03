from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# ========= One To One =========
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


# ========= Foreign Key (One To Many) =========
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


# ========= Many To Many =========
class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="courses")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

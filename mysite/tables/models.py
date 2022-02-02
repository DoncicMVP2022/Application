import django
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Specialist(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS = (
        ("To do", "To do"),
        ("In progress", "In progress"),
        ("In review", "In review"),
        ("Done", "Done"),
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    task_status = models.CharField(max_length=200, null=True, choices=STATUS)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Projects(models.Model):
    STATUS = (
        ("To do", "To do"),
        ("In progress", "In progress"),
        ("In review", "In review"),
        ("Done", "Done"),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ManyToManyField(Task)
    specialist = models.ManyToManyField(Specialist)
    project_status = models.CharField(max_length=200, null=True, choices=STATUS)
    data_created = models.DateTimeField(null=True, default=django.utils.timezone.now)

    def __str__(self):
        return self.name


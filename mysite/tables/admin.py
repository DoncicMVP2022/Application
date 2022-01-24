from django.contrib import admin
from .models import Task, Projects, Specialist

admin.site.register((Task, Projects, Specialist))

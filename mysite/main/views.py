from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from tables.models import Projects


@login_required(login_url='login')
@admin_only
def home(request):
    projects = Projects.objects.all()
    total_projects = projects.count()
    total_to_do_projects = projects.filter(project_status="To do").count()
    total_close_projects = projects.filter(project_status="Done").count()
    context = {'projects': projects, 'total_projects': total_projects, 'total_to_do_projects':
        total_to_do_projects, 'total_close_projects': total_close_projects}
    return render(request, 'main/main.html', context)

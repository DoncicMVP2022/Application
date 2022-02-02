from django.shortcuts import render, redirect
from .forms import TaskTableForm, SpecialistForm, ProjectsForm
from .models import Task, Projects, Specialist
from .filters import ProjectFilter
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users


@login_required(login_url='login')
def Dashboard(request, pk_task):
    group = request.user.groups.all()[0].name
    projects = Projects.objects.get(id=pk_task)
    specialists = projects.specialist.all()
    task = projects.task.all()
    total_task = projects.task.count()
    total_cooperator = projects.specialist.count()
    total_close_task = projects.task.filter(task_status="Done").count()
    context = {
        "total_task": total_task,
        "total_cooperator": total_cooperator,
        "specialists": specialists,
        'task': task,
        'projects': projects,
        'total_close_task': total_close_task,
        'group': group
    }
    return render(request, 'tables/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def SpecialistListView(request):
    specialist = Specialist.objects.all()
    context = {'specialists': specialist}
    return render(request, 'tables/specialist_view.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin, teamlead'])
def DeleteSpecialist(request, pk):
    specialist = Specialist.objects.get(id=pk)
    if request.method == "POST":
        specialist.delete()
        return redirect('home')
    context = {'item': specialist}
    return render(request, 'tables/specialist_delete.html', context)


@login_required(login_url='login')
def CooperatorView(request, pk_test):
    cooperator = Specialist.objects.get(id=pk_test)
    projects = Projects.objects.filter()
    projects = projects.filter(specialist=cooperator)
    projects_count = projects.count()
    myFilter = ProjectFilter(request.GET, queryset=projects)
    tasks = myFilter.qs
    context = {'cooperator': cooperator, 'tasks': tasks, 'myFilter': myFilter,
               "projects_count": projects_count}
    return render(request, 'tables/cooperator.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin, teamlead'])
def UpdateSpecialist(request, pk):
    specialist = Specialist.objects.get(id=pk)
    form = SpecialistForm()
    if request.method == "POST":
        form = SpecialistForm(request.POST, instance=specialist)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'specialist': specialist}
    return render(request, 'tables/specialist_update.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def CreateTaskTable(request, pk):
    project = Projects.objects.get(id=pk)
    form = TaskTableForm()
    if request.method == "POST":
        form = TaskTableForm(request.POST)
        if form.is_valid():
            task = form.save()
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            task_status = form.cleaned_data.get('task_status')
            task = Task(
                name=name,
                description=description,
                task_status=task_status
            )
            task.save()
            project.task.add(task)
            return redirect('home')
    context = {"project": project, 'form': form}
    return render(request, 'tables/create_task.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def CreateProjects(request):
    form = ProjectsForm()
    if request.method == "POST":
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, "tables/create_projects.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def UpdateProjects(request, pk):
    project = Projects.objects.get(id=pk)
    form = ProjectsForm(instance=project)
    if request.method == "POST":
        form = TaskTableForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tables/task_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def DeleteProject(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('home')
    context = {'item': project}
    return render(request, 'tables/project_delete.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin', 'teamlead'])
def UpdateTableTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskTableForm(instance=task)
    if request.method == "POST":
        form = TaskTableForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'tables/task_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'teamlead'])
def DeleteTableTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    context = {'item': task}
    return render(request, 'tables/task_delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['specialist'])
def userPage(request):
    all_projects = Projects.objects.all()
    projects = request.user.specialist.projects_set.all()
    total_to_do_projects = projects.filter(project_status="To do").count()
    total_close_projects = projects.filter(project_status="Done").count()
    total_project = projects.count()
    context = {'projects': projects,
               'total_projects': total_project,
               'total_to_do_projects': total_to_do_projects,
               'total_close_projects': total_close_projects
               }
    return render(request, 'tables/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['specialist', 'teamlead'])
def accountSettings(request):
    form = {}
    try:
        specialist = Specialist.objects.get(user=request.user)

        form = SpecialistForm(instance=specialist)

        if request.method == "POST":
            form = SpecialistForm(request.POST, request.FILES, instance=specialist)
            if form.is_valid():
                form.save()
    except Specialist.DoesNotExist as e:
        print(e)

    context = {'form': form}
    return render(request, 'tables/account_settings.html', context)

from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from tables.models import Specialist


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group_name = form.cleaned_data.get('groups').get()
            group = Group.objects.get(name=group_name)
            user.groups.add(group)

            Specialist.objects.create(
                user=user,
                name=user.username
            )



            messages.success(request, 'Account was created for' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'authentication/registration.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'authentication/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

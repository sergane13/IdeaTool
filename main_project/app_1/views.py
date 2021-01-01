from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_function(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'app_1/register.html', context)


def login_function(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorect')

    context = {}
    return render(request, 'app_1/login.html', context)


def logout_function(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_function(request):

    temp = Idea.objects.all()
    length = Idea.objects.count()

    context = {
        'temp': temp,
        'length': length,
    }
    return render(request, 'app_1/home.html', context)


@login_required(login_url='login')
def idea_create(request):

    form = CreateIdeaForm()
    if request.method == 'POST':
        form = CreateIdeaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Idea sheet was created successfully')
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'app_1/idea_form.html', context)


@login_required(login_url='login')
def idea_update(request, pk):

    idea = Idea.objects.get(id=pk)
    form = CreateIdeaForm(instance=idea)

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'app_1/idea_form.html', context)


@login_required(login_url='login')
def idea_update_optimism(request, pk):

    idea = Idea.objects.get(id=pk)
    form = CreateIdeaForm(instance=idea)

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'app_1/optimism.html', context)


@login_required(login_url='login')
def idea_update_neutralism(request, pk):

    idea = Idea.objects.get(id=pk)
    form = CreateIdeaForm(instance=idea)

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'app_1/neutralism.html', context)


@login_required(login_url='login')
def idea_delete(request, pk):

    idea = Idea.objects.get(id=pk)

    if request.method == 'POST':
        idea.delete()
        return redirect('home')

    context = {
        'item': idea
    }
    return render(request, 'app_1/delete_idea.html', context)

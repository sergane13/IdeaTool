# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import *
from django.contrib import messages


@login_required(login_url="/login/")
def index(request):
    temp = Idea.objects.all()
    context = {
        'temp': temp,
    }
    return render(request, "index.html", context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def idea_form(request, title):

    idea = Idea.objects.get(title=title)
    form = CreateIdeaForm(instance=idea)

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'idea_form.html', context)


@login_required(login_url='login')
def idea_delete(request, title):

    idea = Idea.objects.get(title=title)

    if request.method == 'POST':
        idea.delete()
        return redirect('home')

    context = {
        'item': idea
    }
    return render(request, 'idea_delete.html', context)


@login_required(login_url='login')
def idea_create(request):

    form = CreateIdeaForm()

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST)

        title = request.POST.get("title")
        temp = Idea.objects.filter(title=title).count()

        if form.is_valid() and not temp and title is not '':
            form.save()
            return redirect('home')
        elif title is '':
            messages.info(request, 'Idea must have a name')
        else:
            messages.info(request, 'This name already exists')

    context = {
        'form': form,
    }
    return render(request, 'idea_form_create.html', context)


@login_required(login_url='login')
def idea_view(request, title):
    idea = Idea.objects.get(title=title)

    context = {
        'idea': idea
    }
    return render(request, 'idea_view.html', context)


'''
def cookies_are_life(request):
    color = ''
    if 'bk-color' in request.COOKIES:
        color = request.COOKIES['bk-color']

    return color
'''
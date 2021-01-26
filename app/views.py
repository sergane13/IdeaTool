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
from django.urls import reverse
import stripe

stripe.api_key = 'sk_test_51IDRYEHkebrglgsgXHP1dECWUjp46cERZfS0Vp0H2VRzttjEbpW25TB7sbpkN5WFnTr3XbKEcrQuPuLMWlWeQA7G00R2OB0LKe'


"""
index ---> main page with all the 'Idea' objects
"""


@login_required(login_url="/login/")
def index(request):
    temp = Idea.objects.all()
    context = {
        'temp': temp,
    }
    return render(request, "index.html", context)


"""
error pages
"""


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

        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


"""

Idea functions

1.idea_create ---> create the 'Idea' object
2.idea_form ---> modify the 'Idea' object
3.idea_view ---> view the 'Idea' object
4.idea_delete ---> delete the 'Idea' object

"""


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


@login_required(login_url="/login/")
def idea_form(request, title):

    idea = Idea.objects.get(title=title)
    opinions = Opinions.objects.filter(idea_opinion=idea)

    form = CreateIdeaForm(instance=idea)

    if request.method == 'POST':
        form = CreateIdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'title': title,
        'opinions': opinions,
    }
    return render(request, 'idea_form.html', context)


@login_required(login_url='login')
def idea_view(request, title):
    idea = Idea.objects.get(title=title)
    opinions = Opinions.objects.filter(idea_opinion=idea)

    context = {
        'idea': idea,
        'opinions': opinions,
    }
    return render(request, 'idea_view.html', context)


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


"""

########################END IDEA FUNCTIONS##############################

"""

"""

Opinion functions

1.opinion_create ---> create the 'Opinions' object
2.opinion_view ---> view the 'Idea' object
3.opinion_delete ---> delete the 'Opinions' object

"""


@login_required(login_url='login')
def opinion_create(request, title):

    form = CreateOpinionForm()
    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('opinion')
        opinion = Idea.objects.get(title=title)

        Opinions.objects.create(
            name=name,
            opinion=description,
            idea_opinion=opinion,
        )
        return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'opinions/opinion_create.html', context)


@login_required(login_url='login')
def opinion_view(request, title, opinion):

    idea = Idea.objects.get(title=title)
    temp = Opinions.objects.get(name=opinion, idea_opinion=idea)

    main_name = temp.name

    form = CreateOpinionForm(instance=temp)

    if request.method == 'POST':
        form = CreateOpinionForm(request.POST, instance=temp)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'title': title,
        'main_name': main_name,
    }
    return render(request, 'opinions/opinion_view.html', context)


@login_required(login_url='login')
def opinion_delete(request, title, opinion):

    temp = Idea.objects.get(title=title)
    idea = Opinions.objects.get(name=opinion, idea_opinion=temp)

    if request.method == 'POST':
        idea.delete()
        return redirect('home')

    context = {
        'item': idea,
        'title': title,
    }
    return render(request, 'opinions/opinion_delete.html', context)


"""

########################END OPINIONS FUNCTIONS##############################

"""

"""

Payment

"""


@login_required(login_url='login')
def payment_offers(request):
    return render(request, 'payments/offers_page.html')


@login_required(login_url='login')
def payment(request, amount):
    context = {
        'amount': amount
    }
    return render(request, 'payments/payment_page.html', context)


@login_required(login_url='login')
def successful(request):
    return render(request, 'payments/success.html')


@login_required(login_url='login')
def charge(request, amount):

    if request.method == 'POST':

        total_cash = int(round(float(amount)))

        customer = stripe.Customer.create(
            name=request.POST['nickname'],
            email=request.user.email,
            source=request.POST['stripeToken'],
        )

        stripe.Charge.create(
            customer=customer,
            amount=total_cash * 100,
            currency='usd',
            description='Standard subscription'
        )
    return redirect(reverse('payment_successful'))

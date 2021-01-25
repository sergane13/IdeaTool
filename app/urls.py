# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('idea_form/<str:title>', views.idea_form, name='idea_form'),
    path('idea_delete/<str:title>', views.idea_delete, name='idea_delete'),
    path('idea_create', views.idea_create, name='idea_create'),
    path('idea_view/<str:title>', views.idea_view, name='idea_view'),
    path('charge/<str:amount>', views.charge, name="charge"),
    path('payment_offers', views.payment_offers, name='offers'),
    path('payment/<str:amount>', views.payment, name='payment'),
    path('payment_successful', views.successful, name='payment_successful'),
]

# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.contrib.auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this

    path('reset_password/', PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]

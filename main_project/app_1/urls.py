from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_function, name='register'),
    path('login/', views.login_function, name='login'),
    path('logout/', views.logout_function, name='logout'),
    path('idea_form/', views.idea_create, name='idea_form'),
    path('idea_form_update/<str:pk>', views.idea_update, name='idea_form_update'),
    path('idea_form_update_optimism/<str:pk>', views.idea_update_optimism, name='idea_form_update_optimism'),
    path('idea_form_update_neutralism/<str:pk>', views.idea_update_neutralism, name='idea_form_update_neutralism'),
    path('idea_form_delete/<str:pk>', views.idea_delete, name='idea_form_delete'),
    path('', views.home_function, name='home'),
]

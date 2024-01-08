from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.projects,name='home'),
    path('create-project/', views.project_creator, name="create-form"),
    path('update-project/<str:pk>', views.project_update, name="update-form"),
    path('delete/<str:pk>', views.project_delete, name="delete")
]

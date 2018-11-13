from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('view-all/', views.view_all),
]

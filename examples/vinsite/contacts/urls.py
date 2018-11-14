from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view-all/', views.view_all, name='view_all'),
    path('view-details/<int:id>', views.view_details, name='view_details'),
    path('contact-form/', views.contact_form, name='contact_form'),
    path('save-contact/', views.save_contact, name='save_contact'),

]

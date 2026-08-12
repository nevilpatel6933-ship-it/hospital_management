from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),

    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/edit/<int:id>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:id>/', views.doctor_delete, name = 'doctor_delete'),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add', views.patient_create, name = 'patient_create'),
    path('patients/edit/<int:id>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:id>', views.patient_delete, name='patient_delete'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add', views.appointment_create, name = 'appointment_create'),
    path('appointments/edit/<int:id>/', views.appointment_update, name='appointment_update'),
    path('appointments/delete/<int:id>', views.appointment_delete, name='appointment_delete'),
]
from django import forms
from .models import Doctor , Patient, Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient   # automatically creates models
        fields = "__all__"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
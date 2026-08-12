from django.shortcuts import render,redirect, get_object_or_404
from .models import Doctor, Patient , Appointment
from .forms import DoctorForm,PatientForm,AppointmentForm

# Create your views here.

def home(request):
    context = {
        "doctor_count" : Doctor.objects.count(),
        "patient_count": Patient.objects.count(),
        "appointment_count": Appointment.objects.count(),
    }
    print("context",context)

    return render (request, 'hospital/home.html', context)


#----------------------------
#DOCTOR CRUD
#----------------------------
def doctor_list(request):

    doctors = Doctor.objects.all()

    context = {
        "doctors":doctors
    }
    print("context",context)
    return render (request, 'hospital/doctor_list.html', context)

def doctor_create(request):

    if request.method == "POST":
        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("doctor_list")

    else:
        form = DoctorForm()

        context = {
            'form':form
        }

        return render(request, 'hospital/doctor_form.html', context)

def doctor_update(request,id):
    doctor = get_object_or_404(Doctor, id = id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            return redirect("doctor_list")

    else:
        form = DoctorForm(instance=doctor)

        context = {
            "form":form
        }

        return render(request, 'hospital/doctor_form.html', context)

def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == "POST":

        doctor.delete()
        return redirect('doctor_list')

    context = {
        'doctor':doctor
    }

    return render (request, 'hospital/doctor_delete.html', context)

#----------------------------
#Patient CRUD
#----------------------------

def patient_list(request):
    patients = Patient.objects.all()

    context = {
        "patients":patients
    }

    return render(request, 'hospital/patient_list.html', context)

def patient_create(request):

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_list")

    else:
        form = PatientForm()

        context = {
            "form":form
        }

        return render(request, 'hospital/patient_form.html', context)

def patient_update(request,id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect("patient_list")

    else:
        form = PatientForm(instance=patient)

        context = {
            "form":form
        }

        return render(request, "hospital/patient_form.html", context)

def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == "POST":

        patient.delete()
        return redirect('patient_list')

    context = {
        "patient":patient
    }

    return render(request,'hospital/patient_delete.html', context)

#----------------------------
# Appointment CRUD
#----------------------------

def appointment_list(request):

    appointments = Appointment.objects.all()
    print("=============================")
    print("appoinment",appointments)
    context = {
        "appointments":appointments
    }

    return render(request,'hospital/appointment_list.html', context)

def appointment_create(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('appoinement_list')

    else:
        form = AppointmentForm()

        context = {
            "form" : form
        }

        return render(request, 'hospital/appointment_form.html', context)

def appointment_update(request):

    appointment = get_object_or_404(Appointment, id = id )

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()

            return redirect("appointment_list")

    else:
        form = AppointmentForm(instance=appointment)

        context = {
            "form":form
        }

        return render (request,'hospital/appointment_form', context)

def appointment_delete(request):

    appointment = get_object_or_404(Appointment, id=id)
    print("Delete appoinment")
    if request.method == "POST":

        appointment.delete()
        return redirect("appointment_list")

    context = {
        "appointment":appointment
    }

    return render(request, 'hospital/appointment_delete.html', context)
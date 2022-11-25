from django.urls import path
from .views import DoctorList, PatientAppointmentList

urlpatterns = [
    path("doctor/", DoctorList.as_view()),
    path("patient/", PatientAppointmentList.as_view()),
]

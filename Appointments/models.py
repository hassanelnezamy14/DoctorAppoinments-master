from unittest import result
from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor_name

class AppoinmentPatient(models.Model):
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='Doctor', null=True, blank=True, unique=True)
    patient_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

  




from rest_framework import serializers
from .models import Doctor, AppoinmentPatient
import re

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class  AppoinmentPatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  AppoinmentPatient
        fields = ["doctor_name","patient_name","phone_no","email","address","created_on"]

    def update(self, instance, validated_data):
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.save()
        return instance

    def validate_phone_no(self, value):
        if (len(value)<=9):
            raise serializers.ValidationError("Mobile muner cannot be less than 10 digit")
        elif(len(value)>10):
            raise serializers.ValidationError("Mobile muner cannot be greater than 10 digit")
        return value
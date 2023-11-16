from rest_framework import serializers
from core.models import Apointment, Department, Doctor


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        exclude = ['created_at', 'updated_at', 'slug']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apointment
        exclude = ['uuid']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ['created_at', 'updated_at', 'slug']

        
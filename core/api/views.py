from core.api.serializers import AppointmentSerializer, DepartmentSerializer, DoctorSerializer
from rest_framework.response import Response
from core.models import Department, Doctor, Apointment
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail

@api_view(['POST'])
def add_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        serializer.data, 
        status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(
        serializer.data, status=status.HTTP_200_OK)



from django.contrib import admin
from .models import Department, Doctor, Patient, Apointment, Contact

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']

@admin.register(Apointment)
class ApointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'doctor', 'date', 'time', 'email', 'phone_no', 'message']
    list_filter = ['date', 'time']
    search_fields = ['name', 'doctor', 'date', 'time', 'email', 'phone_no', 'message']
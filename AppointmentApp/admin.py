from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'appointment_date', 'status', )
    list_filter = ('status', 'doctor', 'appointment_date',)
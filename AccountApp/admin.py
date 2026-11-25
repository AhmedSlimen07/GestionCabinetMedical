from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Doctor, Patient, Specialty, User

admin.site.register(User, UserAdmin)
admin.site.register(Specialty)

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'license_number', 'phone')
    filter_horizontal = ('specialties',)

    def get_readonly_fields(self, request, obj=None):
        return ('license_number',) if obj else ()


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'national_id', 'phone')

    def get_readonly_fields(self, request, obj=None):
        return ('national_id',) if obj else ()

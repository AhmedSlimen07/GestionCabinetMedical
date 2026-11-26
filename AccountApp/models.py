from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    pass

Phone_validator = RegexValidator(r'^\d{8}$', message="Le numéro de téléphone doit contenir exactement 8 chiffres.")

Cin_validator = RegexValidator(r'^\d{8}$', message="Le CIN doit contenir exactement 8 chiffres.")

def validate_past_date(d):
    if d >= timezone.localdate():
        raise ValidationError("La date de naissance doit être antérieure à la date du jour.")

class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone = models.CharField(max_length=8, validators=[Phone_validator])
    specialties = models.ManyToManyField("AccountApp.Specialty", related_name='Doctors')
    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"
    def __str__(self):
        return f"Dr {self.first_name} {self.last_name}"
    
class Patient(User):
    national_id = models.CharField(max_length=8,unique=True,validators=[Cin_validator])
    phone = models.CharField(max_length=8, validators=[Phone_validator])
    birth_date = models.DateField(validators=[validate_past_date])
    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name = "specialty"
        verbose_name_plural = "specialties"
    def __str__(self):
        return self.name
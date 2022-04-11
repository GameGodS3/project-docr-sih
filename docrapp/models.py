from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40)
    age = models.IntegerField()
    blood = models.CharField(max_length=8)
    place = models.CharField(max_length=70)
    dob = models.DateField()

class History(models.Model):
    pref = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hid = models.IntegerField(primary_key=True)
    h_date = models.DateField()
    diagnosis = models.CharField(max_length=150)


class Prescription(models.Model):
    prid = models.IntegerField(primary_key=True)
    href = models.ForeignKey(History, on_delete=models.CASCADE)
    ppref = models.ForeignKey(Patient,on_delete=models.CASCADE)
    pname = models.CharField(max_length=150)
    qty = models.CharField(max_length=20)
    routine = models.CharField(max_length=8)
    duration = models.CharField(max_length=20)
    scan_image  = models.ImageField()

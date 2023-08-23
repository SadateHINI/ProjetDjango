from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    numero=models.PositiveIntegerField()
    is_etudiant = models.BooleanField(default=False)
    is_enseignat = models.BooleanField(default=False)
    is_administrateur = models.BooleanField(default=False)

class Etudiant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    cours=models.CharField(max_length=3000)
    instructeur=models.CharField(max_length=3000)
    filiere=models.CharField(max_length=3000)
    anneeAcademique=models.CharField(max_length=3000)

class Enseignant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    cours=models.CharField(max_length=3000)

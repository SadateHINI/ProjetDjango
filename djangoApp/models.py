from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator 
import datetime

def validate_file_size(value):
    max_size = 5 * 1024 * 1024  # 5 Mo en octets
    if value.size > max_size:
        raise ValidationError('La taille du fichier ne peut pas dépasser 5 Mo.')



# Create your models here.


# class Etudiant(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     nomEtudiant=models.CharField(max_length=3000,null=True)
#     cours=models.CharField(max_length=3000)
#     instructeur=models.CharField(max_length=3000)
#     filiere=models.CharField(max_length=3000)
#     anneeAcademique=models.CharField(max_length=3000)

# class Enseignant(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
#     cours=models.CharField(max_length=3000)


class Matiere(models.Model):
    nomMatiere=models.CharField(max_length=3000)
    
    def __str__(self):
     return self.nomMatiere

class Filiere(models.Model):
    nomFiliere=models.CharField(max_length=3000)
    matieres = models.ManyToManyField(Matiere)

    def __str__(self):
     return self.nomFiliere


class User(AbstractUser):
    numero=models.PositiveIntegerField(null=True)
    is_etudiant = models.BooleanField(null=True)
    is_enseignat = models.BooleanField(null=True)
    is_administrateur = models.BooleanField(null=True)
    filire_etudiant = models.ForeignKey(Filiere, null=True, on_delete=models.SET_NULL)
    matiere_enseignant = models.ManyToManyField(Matiere)

    def __str__(self):
     return self.username


class Projet(models.Model):
    # etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True,)
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    matiere=models.ForeignKey(Matiere,on_delete=models.CASCADE,)
    intituleProjet=models.CharField(max_length=3000)
    fichierProjet=models.FileField(upload_to='devoirs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), validate_file_size])
    description=models.TextField()
    date_creation = models.DateField(default=datetime.date.today)
    deadline = models.DateField(null=True)
    devoir_soumis=models.FileField(upload_to='devoirs_soumis/',  null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), validate_file_size])

    def __str__(self):
        return self.intituleProjet, self.matiere, self.fichierProjet,self.description,self.date_creation,self.deadline

class Devoir(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE,)
    date_soumission = models.DateTimeField(default=datetime.date.today)
    fichier_soumis = models.FileField(upload_to='devoirs_soumis/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), validate_file_size])
    commentaires = models.TextField()
    def __str__(self):
        return f"{self.etudiant} - {self.projet}"


class Projettest(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    intituleProjet = models.CharField(max_length=3000)
    fichierProjet = models.FileField(upload_to='devoirs/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), validate_file_size])
    description = models.TextField()
    date_creation = models.DateField(default=datetime.date.today)
    deadline = models.DateField(null=True)
    devoir_soumis = models.FileField(upload_to='devoirs_soumis/', null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), validate_file_size])

    def __str__(self):
        return self.intituleProjet


class Matieretest(models.Model):
    nomMatiere = models.CharField(max_length=3000)
    projets = models.ManyToManyField(Projettest) 



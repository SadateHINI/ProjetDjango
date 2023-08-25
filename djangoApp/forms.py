from django import forms
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import User, Filiere, Matiere,Projet,Devoir

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "forms-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'is_administrateur', 'is_etudiant', 'is_enseignat','numero')
        
class MatieresCheckboxSelect(forms.CheckboxSelectMultiple):
    def label_from_instance(self, matiere):
        return matiere.nomMatiere

class FiliereForm(forms.ModelForm):
    matieres = forms.ModelMultipleChoiceField(
        queryset=Matiere.objects.all(),
        widget=MatieresCheckboxSelect,
        label="Matieres associées"
    )
    class Meta:
        model = Filiere
        fields = ['nomFiliere', 'matieres']

class ProjetForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields=['matiere', 'intituleProjet', 'fichierProjet', 'description','deadline']


class DevoirForm(forms.ModelForm):
    class Meta:
        model = Devoir
        fields = ['fichier_soumis', 'commentaires']
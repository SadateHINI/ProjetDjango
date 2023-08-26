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
                  'is_administrateur', 'is_etudiant', 'is_enseignat','numero','filire_etudiant','matiere_enseignant')
        
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


class ProjettestForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields=['intituleProjet', 'fichierProjet', 'description','deadline']


class SignUpFormEnseignant(UserCreationForm):
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

    # matiere_enseignant = forms.ModelMultipleChoiceField(
    #     queryset=Matiere.objects.all(),
    #     widget=MatieresCheckboxSelect,
    #     required=False  # Si vous voulez que ce champ ne soit pas obligatoire
    # )

    matiere_enseignant = forms.ModelMultipleChoiceField(
        queryset=Matiere.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Matieres associées"
    )
    

    is_enseignat = forms.BooleanField(initial=True, required=True, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
            'is_enseignat','numero','matiere_enseignant')


class SignUpFormEtudiant(UserCreationForm):
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

    is_etudiant = forms.BooleanField(initial=True, required=True, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
            'is_etudiant','numero','filire_etudiant')
        

class SignUpFormAdimin(UserCreationForm):
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

    is_administrateur = forms.BooleanField(initial=True, required=True, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
            'is_administrateur','numero',)


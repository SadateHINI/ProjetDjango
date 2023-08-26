from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,View
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Matiere, Filiere,Projet,Devoir,Matieretest
from .forms import FiliereForm,ProjetForm,DevoirForm,SignUpFormEnseignant,SignUpFormEtudiant,SignUpFormAdimin
# Create your views here.


def index(request):
    return render(request, 'index.html')


def registerFunction(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'djangoApp/registerPage.html', {'form': form, 'msg': msg})


def loginFunction(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_administrateur:
                login(request, user)
                return redirect('adminpage')
            # elif user is not None and user.is_etudiant:
            #     login(request, user)
            #     return redirect('etudiantPage')
            elif user is not None and user.is_enseignat:
                login(request, user)
                return redirect('enseignant')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'djangoApp/loginPage.html', {'form': form, 'msg': msg})


# MATIERE CRUD
class MatiereCreateView(CreateView):
    model=Matiere
    fields=['nomMatiere']
    template_name='register/matiere_form.html'
    success_url=reverse_lazy('matiere-list')

class MatiereUpdateView(UpdateView):
    model=Matiere
    fields = ['nomMatiere']
    template_name = 'register/matiere_form.html'
    success_url= reverse_lazy('matiere-list')

class MatiereDeleteView(DeleteView):
    model = Matiere
    template_name='register/matiere_confirm_delete.html'
    success_url = reverse_lazy('matiere-list')

class MatiereListView(ListView):
    model = Matiere
    template_name= 'register/matiere_list.html'
    context_object_name='matieres'


# FILIERE CRUD
class FiliereCreateView(CreateView):
    model=Filiere
    form_class = FiliereForm
    # fields=['nomFiliere','matieres']
    template_name='register/filiere_form.html'
    success_url=reverse_lazy('filiere-list')

class FiliereUpdateView(UpdateView):
    model=Filiere
    form_class = FiliereForm
    # fields = ['nomFiliere','matieres']
    template_name = 'register/filiere_form.html'
    success_url= reverse_lazy('filiere-list')

class FiliereDeleteView(DeleteView):
    model = Filiere
    template_name='register/filiere_confirm_delete.html'
    success_url = reverse_lazy('filiere-list')

class FiliereListView(ListView):
    model = Filiere
    template_name= 'register/filiere_list.html'
    context_object_name='filieres'

# PROJET CRUD
class ProjetCreateView(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'register/projet_form.html'
    success_url = reverse_lazy('projet-list')

class ProjetUpdateView(UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'register/projet_form.html'
    success_url = reverse_lazy('projet-list')

class ProjetListView(ListView):
    model = Projet
    template_name = 'register/projet_list.html'

class ProjetDeleteView(DeleteView):
    model = Projet
    template_name = 'register/projet_confirm_delete.html'
    success_url = reverse_lazy('projet-list')

class ProjetDownloadView(View):
    def get(self, request, pk):
        projet = get_object_or_404(Projet, pk=pk)
        return FileResponse(projet.fichierProjet)


# class ProjetShowView(View):
#     template_name = 'projet_show.html'

#     def get(self, request, pk):
#         projet = get_object_or_404(Projet, pk=pk)
#         context = {'projet': projet}
#         return render(request, self.template_name, context)

def ProjetShowView(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    devoir_form = DevoirForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        # Etudiant.nomEtudiant = request.user.username
        if devoir_form.is_valid():
            devoir = devoir_form.save(commit=False)
            devoir.etudiant=request.user  # L'étudiant actuellement connecté
            devoir.projet = projet
            devoir.save()
            return redirect('projet-soumission')

    context = {
        'projet': projet,
        'devoir_form': devoir_form,
    }
    return render(request, 'register/projet_show.html', context)

def liste_matiere(request):
    liste = Matieretest.objects.all().values()
    context = {
        'listes':liste
    }
    return render(request , 'register/liste_matiere.html', context)

def soummission(request):
    return render(request, 'register/projet_soumission.html')

def admin(request):
    return render(request, 'djangoApp/index.html')


def etudiant(request):
    return render(request, 'djangoApp/login.html')


def enseignant(request):
    return render(request, 'djangoApp/profile.html')


def registerEnseignantFunction(request):
    msg = None
    if request.method == 'POST':
        form = SignUpFormEnseignant(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'djangoApp/register_enseignant.html', {'form': form, 'msg': msg})


def registerEtudiantFunction(request):
    msg = None
    if request.method == 'POST':
        form = SignUpFormEtudiant(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'djangoApp/register_etudiant.html', {'form': form, 'msg': msg})


def registerAdminFunction(request):
    msg = None
    if request.method == 'POST':
        form = SignUpFormAdimin(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'djangoApp/register_admin.html', {'form': form, 'msg': msg})


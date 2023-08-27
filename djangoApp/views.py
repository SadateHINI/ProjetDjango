from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,View
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Matiere, Filiere,Projet,Devoir,Matieretest,Cour,User,Devoir
from .forms import FiliereForm,ProjetForm,DevoirForm,SignUpFormEnseignant,SignUpFormEtudiant,SignUpFormAdimin,CourForm
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
                return redirect('AdminAcceuil')
            elif user is not None and user.is_etudiant:
                filiere_etudiant = user.filire_etudiant_id
                matieres_associées = Matiere.objects.filter(filiere__id=filiere_etudiant)
                # matieres_associées = Matiere.objects.filter(filiere_matieres__filiere_id=filiere_etudiant)
                context = {
                    'liste_matiere':matieres_associées
                }
                login(request, user)
                return render(request,'djangoApp/Administrateur/Acceuil_etudiant.html', context)
            elif user is not None and user.is_enseignat:
                id_enseignant  = user.id
                matieres_associées = Matiere.objects.filter(user__id=id_enseignant)
                context = {
                    'liste_matiere':matieres_associées
                }
                login(request, user)
                return render(request,'djangoApp/Administrateur/Acceuil_enseignant.html', context)
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'djangoApp/loginPage.html', {'form': form, 'msg': msg})

def etudiantPage(request):
    return render(request, 'djangoApp/dashBordEtudiant.html')

# MATIERE CRUD
class MatiereCreateView(CreateView):
    model=Matiere
    fields=['nomMatiere']
    template_name='djangoApp/Administrateur/matiere_form.html'
    success_url=reverse_lazy('matiere-list')

class MatiereUpdateView(UpdateView):
    model=Matiere
    fields = ['nomMatiere']
    template_name = 'djangoApp/Administrateur/matiere_form.html'
    success_url= reverse_lazy('matiere-list')

class MatiereDeleteView(DeleteView):
    model = Matiere
    template_name='djangoApp/Administrateur/matiere_confirm_delete.html'
    success_url = reverse_lazy('matiere-list')

class MatiereListView(ListView):
    model = Matiere
    template_name= 'djangoApp/Administrateur/matiere_list.html'
    context_object_name='matieres'


# FILIERE CRUD
class FiliereCreateView(CreateView):
    model=Filiere
    form_class = FiliereForm
    # fields=['nomFiliere','matieres']
    template_name='djangoApp/Administrateur/filiere_form.html'
    success_url=reverse_lazy('filiere-list')

class FiliereUpdateView(UpdateView):
    model=Filiere
    form_class = FiliereForm
    # fields = ['nomFiliere','matieres']
    template_name = 'djangoApp/Administrateur/filiere_form.html'
    success_url= reverse_lazy('filiere-list')

class FiliereDeleteView(DeleteView):
    model = Filiere
    template_name='djangoApp/Administrateur/filiere_confirm_delete.html'
    success_url = reverse_lazy('filiere-list')

class FiliereListView(ListView):
    model = Filiere
    template_name= 'djangoApp/Administrateur/filiere_list.html'
    context_object_name='filieres'

# PROJET CRUD
class ProjetCreateView(CreateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'djangoApp/Administrateur/projet_form.html'
    success_url = reverse_lazy('projet-list')

class ProjetUpdateView(UpdateView):
    model = Projet
    form_class = ProjetForm
    template_name = 'djangoApp/Administrateur/projet_form.html'
    success_url = reverse_lazy('projet-list')

class ProjetListView(ListView):
    model = Projet
    template_name = 'djangoApp/Administrateur/projet_list.html'

class ProjetDeleteView(DeleteView):
    model = Projet
    template_name = 'djangoApp/Administrateur/projet_confirm_delete.html'
    success_url = reverse_lazy('projet-list')

# class ProjetSoumission(ListView):
#     model = Devoir
#     template_name = 'djangoApp/Administrateur/projet_soumission.html'

class DevoirListView(ListView):
    model = Projet
    template_name = 'djangoApp/Administrateur/projet_soumission.html'

class DevoirDownloadView(View):
    def get(self, request, pk):
        devoir = get_object_or_404(Devoir, pk=pk)
        return FileResponse(devoir.fichier_soumis)

class ProjetDownloadView(View):
    def get(self, request, pk):
        projet = get_object_or_404(Projet, pk=pk)
        return FileResponse(projet.fichierProjet)

# COURS CRUD

class CourCreateView(CreateView):
    model = Cour
    form_class = CourForm
    template_name = 'djangoApp/Administrateur/cour_form.html'
    success_url = reverse_lazy('cour-list')

class CourUpdateView(UpdateView):
    model = Cour
    form_class = CourForm
    template_name = 'djangoApp/Administrateur/cour_form.html'
    success_url = reverse_lazy('cour-list')

class CourListView(ListView):
    model = Cour
    template_name = 'djangoApp/Administrateur/cour_list.html'

class CourDeleteView(DeleteView):
    model = Cour
    template_name = 'djangoApp/Administrateur/cour_confirm_delete.html'
    success_url = reverse_lazy('cour-list')

class CourDownloadView(View):
    def get(self, request, pk):
        cour = get_object_or_404(Cour, pk=pk)
        return FileResponse(cour.fichierCour)
    
def CourShowView(request, pk):
    cour = get_object_or_404(Cour, pk=pk)
    model =Cour
    context = {
        'cour': cour,
    }
    
    return render(request, 'djangoApp/Administrateur/cour_show.html', context)


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
    return render(request, 'djangoApp/Administrateur/projet_show.html', context)

def liste_matiere(request):
    liste = Matieretest.objects.all().values()
    context = {
        'listes':liste
    }
    return render(request , 'djangoApp/Administrateur/liste_matiere.html', context)

def soummission(request):
    return render(request, 'djangoApp/Administrateur/projet_soumission.html')

def admin(request):
    return render(request, 'djangoApp/Administrateur/dashBoardAdmin.html')

def etudiant(request):
    return render(request, 'djangoApp/dashBordEtudiant.html')

def enseignant(request):
    return render(request, 'djangoApp/dashBordEnseignant.html')

def listeMatiereEnseignant(request):
    return render(request,'djangoApp/Enseignant/listeMatiereEnseignant.html')

def registerEnseignantFunction(request):
    msg = None
    if request.method == 'POST':
        form = SignUpFormEnseignant(request.POST)
        if form.is_valid():
            user = form.save()
            matieres_selected = form.cleaned_data['matiere_enseignant']
            user.save()  # Sauvegarder l'utilisateur pour obtenir un ID utilisateur
            
            # Ajouter les matières associées à l'utilisateur
            user.matiere_enseignant.set(matieres_selected)
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpFormEnseignant()
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


def liste_enseignants(request):
    enseignants = User.objects.filter(is_enseignant=True)
    context = {'enseignants': enseignants}
    return render(request, 'liste_enseignants.html', context)


def testAdmin(request):
    return render(request, 'djangoApp/Administrateur/test.html')

def testEnseignant(request):
    return render(request, 'djangoApp/Enseignant/test.html')




def AdminAcceuil(request):
    return render(request, 'djangoApp/Administrateur/Acceuil_admin.html')
def EnseignantAcceuil(request):
    return render(request, 'djangoApp/Administrateur/Acceuil_enseignant.html')
def EtudiantAcceuil(request):
    return render(request, 'djangoApp/Administrateur/Acceuil_etudiant.html')


class ProjetListViewEtuduant(ListView):
    model = Projet
    template_name = 'djangoApp/projet_list_etudiant.html'


class CourListViewEtudiant(ListView):
    model = Cour
    template_name = 'djangoApp/cour_liste_etudiant.html'
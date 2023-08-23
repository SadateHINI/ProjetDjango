from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
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


def admin(request):
    return render(request, 'djangoApp/index.html')


def etudiant(request):
    return render(request, 'djangoApp/login.html')


def enseignant(request):
    return render(request, 'djangoApp/profile.html')

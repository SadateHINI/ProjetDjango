from django.contrib import admin
from django.urls import path
from djangoApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerFunction, name="register"),
    # path('inscription/', views.register, name='inscription'),
    path('login/', views.loginFunction, name='login'),
    path('adminpage/', views.admin, name='adminpage'),
    path('etudiant/', views.etudiant, name='etudiantPage'),
    path('enseignant/', views.enseignant, name='enseignant'),
]
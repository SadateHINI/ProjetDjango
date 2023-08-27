# Generated by Django 4.1.4 on 2023-08-26 23:14

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import djangoApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('numero', models.PositiveIntegerField(null=True)),
                ('is_etudiant', models.BooleanField(null=True)),
                ('is_enseignat', models.BooleanField(null=True)),
                ('is_administrateur', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMatiere', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Projettest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intituleProjet', models.CharField(max_length=3000)),
                ('fichierProjet', models.FileField(upload_to='devoirs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('description', models.TextField()),
                ('date_creation', models.DateField(default=datetime.date.today)),
                ('deadline', models.DateField(null=True)),
                ('devoir_soumis', models.FileField(null=True, upload_to='devoirs_soumis/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intituleProjet', models.CharField(max_length=3000)),
                ('fichierProjet', models.FileField(upload_to='devoirs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('description', models.TextField()),
                ('date_creation', models.DateField(default=datetime.date.today)),
                ('deadline', models.DateField(null=True)),
                ('devoir_soumis', models.FileField(null=True, upload_to='devoirs_soumis/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Matieretest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMatiere', models.CharField(max_length=3000)),
                ('projets', models.ManyToManyField(to='djangoApp.projettest')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFiliere', models.CharField(max_length=3000)),
                ('matieres', models.ManyToManyField(to='djangoApp.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_soumission', models.DateTimeField(default=datetime.date.today)),
                ('fichier_soumis', models.FileField(upload_to='devoirs_soumis/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('commentaires', models.TextField()),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.projet')),
            ],
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intituleCour', models.CharField(max_length=3000)),
                ('fichierCour', models.FileField(upload_to='devoirs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']), djangoApp.models.validate_file_size])),
                ('description', models.TextField()),
                ('date_creation', models.DateField(default=datetime.date.today)),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='filire_etudiant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangoApp.filiere'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='matiere_enseignant',
            field=models.ManyToManyField(to='djangoApp.matiere'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]

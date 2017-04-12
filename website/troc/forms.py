from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    adresse_mail = forms.EmailField(label="Adresse mail",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)
"""
class PosterForm(forms.Form):
    photo=forms.ImageField(upload_to=content_file_name, blank=True)
    titre= forms.CharField(label="Titre du troc",max_length=50)
    description= forms.CharField(label="Description(300 caratères max)",max_length=300)
    prix= forms.IntegerField(label="Prix")
    localisation=forms.CharField(label="Localisation") #à lier avec la BD

class SearchForm(forms.Form): Menus avec champs proposés
    category=
    Region=
    Departement=
    Ville=
    Prix=
    """

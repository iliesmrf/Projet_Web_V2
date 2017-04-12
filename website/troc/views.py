from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect
from .forms import RegisterForm,ConnexionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
'''
def index(request):
    """Page d'accueil du site"""
    text = """<h1>Bienvenue sur le meilleur site de troc de france!</h1>
              <p>Troquez tout ce que vous voulez et gagner de l'argent sans rien faire !</p>"""
    return HttpResponse(text)
'''
def view_troc(request,id_cat,id_troc):
    """ Vue qui affiche le troc demandé """
    if int(id_troc)>100:
        raise Http404
    return HttpResponse("<h1>Voici le troc numéro {} de la categorie {}!</h1> <p>test affichage argument GET: {}</p>".format(id_troc,id_cat,request.GET['ref']))

def index(request):
    """Page d'accueil du site"""

    return render(request,'index.html')


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        new_login = form.cleaned_data['username']
        new_passwd = form.cleaned_data['password']
        new_adr_mail= form.cleaned_data['adresse_mail']

        user = User.objects.create_user(new_login,new_adr_mail, new_passwd)
        user.save()
        return render(request,"bravo.html",{'login':new_login})
    return render(request,"register.html",locals())

def connexion(request):
    error = False

    if request.method=="POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
            else:
                error=True
    else:
        form = ConnexionForm()
    return render(request,'connect.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
def compte(request):
    return render(request,'compte.html')

def troc_search(request):
    return render(request,'troc_search.html')

"""
def poster(request):
    error = False
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form = UserProfileForm(instance=request.user.get_profile())
        return render_to_response('user_details.html',
                {'user': request.user, 'form': form},
                context_instance=RequestContext(request))
                """

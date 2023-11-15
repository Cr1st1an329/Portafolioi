from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/inicio.html",{})
def biografia(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/biografia.html",{})
def contact(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/contact.html",{})
@login_required
def biografia(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/biografia.html",{})  


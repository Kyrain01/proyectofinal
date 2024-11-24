# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.services.services import getAllImages  #se busca la funcion y se la llama desde services

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = getAllImages() #se llama a la funcion y la guarda en una variable
    favourite_list = []
    

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''): 
        images = getAllImages(search_msg) #se llama a la funcion para obtener las imagenes que coinciden con lo que el usuario busco
        return render(request, 'home.html', {  #renderiza los datos de home.html, el texto que el usuario introdujo en la barra de busqueda e imagenes que corresponde a la busqueda
            'search_msg': search_msg,
            'images': images
        })
    else:
        return redirect('home') # si no hay texto en la busqueda, redirige al home de la web


# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass


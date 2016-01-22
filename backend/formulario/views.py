from django.shortcuts import render

def registro (request):
    return render (request, "formulario/registro.html", {})

def encuesta_completa(request):
    pass
# /egresado/actualizar
def actualizar(request):
    return render (request, "formulario/registro.html", {})

# /egresado/perfil
def actualizar_perfil(request):
     return render (request, "formulario/actualizar_perfil.html", {})

# /egresado/datoslaborales
def actualizar_datoslab(request):
     return render (request, "formulario/actualizar_datoslab.html", {})

# /egresado/empresa
def actualizar_empresa(request):
     return render (request, "formulario/actualizar_empresa.html", {})





# Create your views here.

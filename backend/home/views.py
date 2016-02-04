from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from .actions import Paginador
from perfil.models import PerfilEgresado


# Create your views here.

def index_view(request):
    'pagina principal'
    usuario=request.user
    if usuario.is_anonymous():
        if request.method=='POST':
            #solicitud de login por post
            if True:
                usuariof=request.POST.get('username','')
                clavef=request.POST.get('password','')
                acceso=authenticate(username=usuariof,password=clavef)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        #Pantalla del Perfil
                        return HttpResponseRedirect('/')
                    else:
                        error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
                else:
                    error="El usuario no existe, verifique que este bien escrito"
            else:
                error="Datos invalidos en el formulario"
            ctx={'error':error, 'c_login':'active'}
            return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))
        else:
            #Login
            return render_to_response('home/index.html',
                          {'c_login':'active'},
                          context_instance=RequestContext(request))
    elif usuario.is_staff:
        return HttpResponseRedirect('/home')
    else:
        current_user = request.user
        print current_user.username
        try:
            user = PerfilEgresado.objects.get(num_control=current_user.username)
            return HttpResponseRedirect('/egresado/actualizar')
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/egresado/perfil')


def home(request):
    cxt={}
    if request.method == 'POST':
        filtro_numcontrol = request.POST.get('numcontrol_f','')
        filtro_numcontrol = str(filtro_numcontrol)
        try:
            egresado_numcontrol = PerfilEgresado.objects.get(num_control=filtro_numcontrol)
            cxt = {'egresado_numcontrol':egresado_numcontrol}
        except PerfilEgresado.DoesNotExist :
            msg = "Numero de Control No Encontrado: {0}".format(filtro_numcontrol )
            print msg
            cxt = {'Error': msg}
        
    return render(request,'home/home.html', cxt)

MAXIMO_ITEMS_HOJA = 10
def carrera(request):
    
    cxt={}
    
    if request.method=='POST':
        filtro = request.POST.get("carrera_f", "")
        if filtro == "carrera":
            return redirect('/home/') 
        else:
            egresados = PerfilEgresado.objects.filter(carrera=filtro)
            
            egresados = Paginador(egresados, MAXIMO_ITEMS_HOJA, 1)
            cxt = {'Egresados': egresados,
                valuecarrera(filtro): True, "filtrocarrera":filtro}
            return render(request,'home/home.html', cxt)
    elif request.method=='GET':
        pagina = request.GET.get("pagina", "")
        filtro = request.GET.get("filtro", "")
        if filtro == "carrera":
            return redirect('/home/') 
        else:
            egresados = PerfilEgresado.objects.filter(carrera=filtro)
            
            egresados = Paginador(egresados, MAXIMO_ITEMS_HOJA, pagina)
            cxt = {'Egresados': egresados,
                valuecarrera(filtro): True, "filtrocarrera":filtro}
            return render(request,'home/home.html', cxt)
    else:
        return render(request,'home/home.html', cxt)





def valuecarrera(carrera):
    carrera  = int(carrera)
    if carrera == 1:
        return "selectbio"
    elif carrera == 2:
        return "selectciv"
    elif carrera == 3:
        return "selectelec"
    elif carrera == 4:
        return "selectind"
    elif carrera == 5:
        return "selectmec"
    elif carrera == 6:
        return "selectsis"
    elif carrera == 7:
        return "selectadm"
    elif carrera == 8:
        return "selectcon"
    elif carrera == 9:
        return "selectelem"
    elif carrera == 10:
        return "selectges"
    elif carrera == 11:
        return "selectlog"
    else:
        return  "selectcarrera"
    
  

def info(request):
    return render(request,'home/info.html', {'nombre':'luis'})


@login_required(login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

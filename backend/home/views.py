from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext


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
    else:
        return HttpResponseRedirect('/home')

def home(request):
    return render(request,'home/home.html', {})

def info(request):
    return render(request,'home/info.html', {'nombre':'luis'})

def graficas(request):
    return render(request, 'graficas/graficageneral.html', {})

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

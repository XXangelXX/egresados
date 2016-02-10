from django.forms import ModelForm
from perfil.models import PerfilEgresado, DatosLaborales, Carrera
from empresa.models import Empresa, Encargado
from django.contrib.auth.models import User


class PerfilEgresadoForm(ModelForm):
    class Meta:
        model = PerfilEgresado
       

class DatosLaboralesForm(ModelForm):
    class Meta:
        model = DatosLaborales

class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa

class EncargadoForm(ModelForm):
    class Meta:
        model = Encargado

class UserForm(ModelForm):
    class Meta:
        model = User



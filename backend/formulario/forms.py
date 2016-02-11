from django.forms import ModelForm
from perfil.models import PerfilEgresado, DatosLaborales, Carreras
from empresa.models import Empresa, Encargado
from django.contrib.auth.models import User


class PerfilEgresadoForm(ModelForm):
    class Meta:
        model = PerfilEgresado
        exclude = ["usuario",""]
       

class DatosLaboralesForm(ModelForm):
    class Meta:
        model = DatosLaborales
        exclude = ["egresado"]

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        exclude = ["datoslaborales"]

class EncargadoForm(ModelForm):
    class Meta:
        model = Encargado
        exclude = ["empresa"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]



from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Empresa, Encargado



class EmpresaResource(resources.ModelResource):

    class Meta:
        model = Empresa

class EncargadoResource(resources.ModelResource):

    class Meta:
        model = Encargado


class EncargadoAdmin(ImportExportModelAdmin):
    resource_class = EncargadoResource
    list_display =("nom_encargado","titulo","puesto",)


class EmpresaAdmin(ImportExportModelAdmin):
    resource_class = EmpresaResource
    list_display =("tipo","giro_actividad","razon_social","telefono",)


admin.site.register(Encargado, EncargadoAdmin)
admin.site.register(Empresa, EmpresaAdmin)




# Register your models here.

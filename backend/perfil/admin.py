from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import PerfilEgresado, DatosLaborales, Carreras


class PerfilEgresadoResource(resources.ModelResource):

    class Meta:
        model = PerfilEgresado
        
class DatosLaboralesResource(resources.ModelResource):

    class Meta:
        model = DatosLaborales

class CarrerasResource(resources.ModelResource):

    class Meta:
        model = Carreras

class PerfilEgresadoAdmin(ImportExportModelAdmin):
    resource_class = PerfilEgresadoResource
    list_display =("id","nombre","a_paterno","a_materno","num_control","mes_anio_egreso",
        "especialidad",)

class DatosLaboralesAdmin(ImportExportModelAdmin):
    resource_class = DatosLaboralesResource
    list_display =("egresado","medio_obt_trabajo","req_contratacion","ant_empleo",
        "niv_jerarquico",)

class CarrerasAdmin(ImportExportModelAdmin):
    resource_class = CarrerasResource
    list_display =("id","nombre_carrera",)
    
# Register your models here.
admin.site.register(PerfilEgresado, PerfilEgresadoAdmin)
admin.site.register(DatosLaborales, DatosLaboralesAdmin)
admin.site.register(Carreras,CarrerasAdmin)

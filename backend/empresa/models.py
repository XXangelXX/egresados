# -*- coding: utf-8 -*-
from django.db import models
from perfil.estados import ESTADO_OPTIONS
from perfil.models import DatosLaborales

# Create your models here.
class Empresa(models.Model):

    datoslaborales = models.ForeignKey(DatosLaborales)
    
    PUBLICO = "1"
    PRIVADO = "2"
    SOCIAL = "3"
    TIPO_OPTIONS = (
        (PUBLICO, 'Publico'),
        (PRIVADO, 'Privado'),
        (SOCIAL, 'Social'),
    )
    tipo = models.CharField(max_length=2,
                                      choices=TIPO_OPTIONS)                         
 
    giro_actividad = models.CharField(max_length=50,blank=True)
    razon_social = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50,blank=True)
    cuidad = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)  
    estado = models.CharField(max_length=50, choices=ESTADO_OPTIONS)
    telefono = models.CharField(max_length=15,blank=True)
    fax = models.CharField(max_length=15,blank=True)
    e_mail = models.EmailField(blank=True)
    url = models.URLField(max_length=200,blank=True)
    SP = 'Sector Primario'
    SS = 'Sector Secundario'
    ST = 'Sector Terciario'

    SECTOR_CHOICES = (
        (SP, (
                ('11', 'Agroindustrial'),
                ('12', 'Pesquero'),
                ('13', 'Minero'),
                ('14', 'Otros'),
            )
        ),
        (SS, (
                ('21', 'Industrial'),
                ('22', 'Constructor'),
                ('23', 'Petrolero'),
                ('24', 'Otros'),
            )
        ),
        (ST, (
                ('31', 'Educativo'),
                ('32', 'Turismo'),
                ('33', 'Comercio'),
                ('34', 'Servicios Financieros'),
                ('35', 'Otros'),
            )
        ),

    )
    sector = models.CharField(max_length=2,
                                      choices=SECTOR_CHOICES, 
                                      blank=True)

    MICREMP = "1"
    PEQEMP = "2"
    MEDIEMP = "3"
    GRANEMP = "4"
    TAM_EMPRESA_OPTIONS = (
        (MICREMP, 'Microempresa (1-30)'),
        (PEQEMP, 'Pequeña  (31-100)'),
        (MEDIEMP, 'Mediana (101-500)'),
        (GRANEMP, 'Grande (mas de 500)'),
    
    )
    tam_empresa = models.CharField(max_length=2,
                                      choices=TAM_EMPRESA_OPTIONS)

    POC = "1"
    SIG = "2"
    MOD = "3"
    REG = "4"
    MUCH = "5"
    AREA_ESTUDIO_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    area_estudio = models.CharField(max_length=2,
                                      choices=AREA_ESTUDIO_OPTIONS)

    TITULACION_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    )
    titulacion = models.CharField(max_length=2,
                                      choices=TITULACION_OPTIONS)

    EXP_LAB_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    exp_lab = models.CharField(max_length=2,
                                      choices=EXP_LAB_OPTIONS)

    COMP_LAB_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    comp_lab = models.CharField(max_length=2,
                                      choices=COMP_LAB_OPTIONS)
    
    POSICION_INST_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    posicion_inst = models.CharField(max_length=2,
                                      choices=POSICION_INST_OPTIONS)

    CONOCIM_IDIOMAS_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    conocim_idiomas = models.CharField(max_length=2,
                                      choices=CONOCIM_IDIOMAS_OPTIONS)
   
    RECOMEND_ACTITUD_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    recomend_actitud = models.CharField(max_length=2,
                                      choices=RECOMEND_ACTITUD_OPTIONS)

    PERSONALIDAD_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    personalidad = models.CharField(max_length=2,
                                      choices=PERSONALIDAD_OPTIONS)

    CAP_LIDERAZGO_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    cap_liderazgo = models.CharField(max_length=2,
                                      choices=CAP_LIDERAZGO_OPTIONS)

    OTROS_ASP_OPTIONS = (
        (POC, 'Poco'),
        (SIG, 'Significativo'),
        (MOD, 'Moderado'),
        (REG, 'Regular'),
        (MUCH, 'Mucho'),
    
    )
    otros_asp = models.CharField(max_length=2,
                                      choices=OTROS_ASP_OPTIONS)



    

    def __unicode__(self):
        return self.razon_social



class Encargado (models.Model):
    empresa = models.ForeignKey(Empresa, blank=True)
    
    nom_encargado = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50,blank=True)
    puesto = models.CharField(max_length=50,blank=True)
    

    def __unicode__(self):
        return self.nom_encargado
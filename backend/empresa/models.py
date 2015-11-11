# -*- coding: utf-8 -*-
from django.db import models
from perfil.estados import ESTADO_OPTIONS

# Create your models here.
class Encargado (models.Model):
    nom_encargado = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50,blank=True)
    puesto = models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return self.nom_encargado


class Empresa(models.Model):
    
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

    encargado = models.ForeignKey(Encargado,blank=True)
    

    def __unicode__(self):
        return self.razon_social




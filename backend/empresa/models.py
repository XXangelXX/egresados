from django.db import models

# Create your models here.
class Empresa(models.Model):
    
    PUBLICO = 1
    PRIVADO = 2
    SOCIAL = 3
    TIPO_OPTIONS = (
        (PUBLICO, 'Publico'),
        (PRIVADO, 'Privado'),
        (SOCIAL, 'Social'),
    )
    tipo = models.CharField(max_length=2,
                                      choices=TIPO_OPTIONS,
                                      default=PUBLICO)
    
    giro_actividad = models.CharField(max_length=50)
    razon_social = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    cuidad = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(OPTIONS: {})
    telefono = models.DateField()
    fax = models.DateField()
    e_mail = models.EmailField()
    url = models.URLField(max_length=200)
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
                                      choices=SECTOR_CHOICES)
    titulo = models.CharField(max_length=50)
    nom_encargado = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)

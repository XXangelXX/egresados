from django.db import models
from perfil.models import Empresa

# Create your models here.
class Carreras (models.Model):
    nombre_carrera = models.CharField(max_length=20)

class DatosLaborales (models.Model):
    
    BOLTRABPLAN = '1'
    CONTPER = '2'
    RESPROF ='3'
    MDMSCOM = '4'
    OTROS = '5'
    MEDIO_OBT_TRABAJO_OPTIONS = (
        (BOLTRABPLAN , 'Bolsa de Trabajo del Plantel'),
        (CONTPER, 'Contacto Personales'),
        (RESPROF, 'Residencias Profesionales'),
        (MDMSCOM, 'Medios Masivos de Comunicación'),
        (OTRO, 'Otro'),
    )
    medio_obt_trabajo = models.CharField(max_length=2,
                                      choices=MEDIO_OBT_TRABAJO_OPTIONS,
                                      default=BOLTRABPLAN)

    COMPLAB = '1'
    TITPROF = '2'
    EXASEL ='3'
    IDIEXTR = '4'
    OTROS = '5'
    REQ_CONTR_OPTIONS = (
        (COMPLAB , 'Competencias Laborales'),
        (TITPROF, 'Titulo Profesional'),
        (EXASEL, 'Examen de Selección'),
        (IDIEXTR, 'Idioma Extranjero'),
        (OTRO, 'Otro'),
    )
    req_contratacion = models.CharField(max_length=2,
                                      choices=REQ_CONTR_OPTIONS,
                                      default=COMPLAB)

    MENOS1 = '1'
    UNO = '2'
    DOS ='3'
    TRES = '4'
    MASDETRES = '5'
    ANT_EMPLEO_OPTIONS = (
        (MENOS1 , 'Menos de un año'),
        (UNO, 'Un año'),
        (DOS, 'Dos años'),
        (TRES, 'Tres años'),
        (MASDETRES, 'Mas de Tres años'),
    )
    ant_empleo = models.CharField(max_length=2,
                                      choices=ANT_EMPLEO_OPTIONS,
                                      default=MENOS1)

    año_ingr_laboral = models.DateTimeField()

    TEC = '1'
    SUPRV = '2'
    JFAR ='3'
    FUNC = '4'
    DIRCT = '5'
    EMPR = '5'
    NIV_JERQ_OPTIONS = (
        (TEC , 'Técnico'),
        (SUPRV, 'Supervisor'),
        (JFAR, 'Jefe de Área'),
        (FUNC, 'Funcionario'),
        (DIRCT, 'Directivo'),
        (EMPR, 'Empresario'),
    )
    niv_jerarquico = models.CharField(max_length=2,
                                      choices=NIV_JERQ_OPTIONS,
                                      default=TEC)



class PerfilEgresado(models.Model):
    nombre = models.CharField(max_length=30)
    a_paterno = models.CharField(max_length=30)
    a_materno = models.CharField(max_length=30)
    f_nacimiento = models.DateTimeField()
    
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_OPTIONS = (
        (MASCULINO , 'Masculino'),
        (FEMENINO, 'Femenino'),
    )
    sexo = models.CharField(max_length=2,
                                      choices=SEXO_OPTIONS,
                                      default=MASCULINO)
    curp = models.CharField(max_length=19)
    CASADO = 'C'
    SOLTERO = 'S'
    DIVORCIADO ='D'
    OTRO = 'O'
    EST_CIVIL_OPTIONS = (
        (CASADO , 'Casado(a)'),
        (SOLTERO, 'Soltero(a)'),
        (DIVORCIADO, 'Divorciado(a)'),
        (OTRO, 'Otro'),
    )
    e_civil = models.CharField(max_length=2,
                                      choices=EST_CIVIL_OPTIONS,
                                      default=SOLTERO)
    estado = models.CharField(max_length=30)
    cuidad = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    telefono = models.DateTimeField()
    especialidad = models.DateTimeField()
    c_egreso = models.CharField(max_length=50)
    mes_año_egreso = models.DateTimeField()

    TRABAJA = 1
    ESTUDIA = 2
    TRABAJAYESTUDIA = 3
    NINI = 4
    OCUPACION_OPTIONS = (
        (TRABAJA, 'Trabaja'),
        (ESTUDIA, 'Estudia'),
        (TRABAJAYESTUDIA, 'Trabaja y Estudia'),
        (NINI, 'Ni Trabaja Ni Estudia'),
    )
    ocupacion = models.CharField(max_length=2,
                                      choices=OCUPACION_OPTIONS,
                                      default=TRABAJA)
    carrera = models.ForeignKey(Carreras)

    empresa = models.ForeignKey(Empresa)



    
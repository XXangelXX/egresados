# -*- coding: utf-8 -*-
from django.db import models
from perfil.estados import ESTADO_OPTIONS

# Create your models here.
class Carreras (models.Model):
    nombre_carrera = models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombre_carrera



class PerfilEgresado(models.Model):
    carrera = models.ForeignKey(Carreras)
    #user_login = model.ForeignKey()

    nombre = models.CharField(max_length=30)
    a_paterno = models.CharField(max_length=30)
    a_materno = models.CharField(max_length=30)
    num_control = models.CharField(max_length=9)
    f_nacimiento = models.DateField(blank=True)
    
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
    estado = models.CharField(max_length=30, choices=ESTADO_OPTIONS)
    cuidad = models.CharField(max_length=30)
    municipio = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=20)
    e_mail = models.EmailField(blank=True)
    mes_anio_egreso = models.DateField(blank=True)
    tel_casa = models.CharField(max_length=15)
    niv_ing = models.IntegerField()
    otros_idms = models.CharField(max_length=100)
    man_paq_comp = models.CharField(max_length=200)

    SIT = "1"
    NOT = "0"
    TITULADO_OPTIONS = (
        (SIT, 'Si'),
        (NOT, 'No'),
    )
    titulado = models.CharField(max_length=2,
                                      choices=TITULADO_OPTIONS,
                                      default=SIT)

    TRABAJA = "1"
    ESTUDIA = "2"
    TRABAJAYESTUDIA = "3"
    NINI = "4"
    OCUPACION_OPTIONS = (
        (TRABAJA, 'Trabaja'),
        (ESTUDIA, 'Estudia'),
        (TRABAJAYESTUDIA, 'Trabaja y Estudia'),
        (NINI, 'Ni Trabaja Ni Estudia'),
    )
    ocupacion = models.CharField(max_length=2,
                                      choices=OCUPACION_OPTIONS,
                                      default=TRABAJA)

    ESPECIALIDAD = "1"
    MAESTRIA = "2"
    IDIOMAS = "3"
    OTROS = "4"
    ESTUDIOS_ACT_OPTIONS = (
        (ESPECIALIDAD, 'Especialidad'),
        (MAESTRIA, 'Maestria'),
        (IDIOMAS, 'Idiomas'),
        (OTROS, 'Otros'),
    )
    estudios_act = models.CharField(max_length=2,
                                      choices=ESTUDIOS_ACT_OPTIONS)

    esp_intitucion = models.CharField(max_length=50)


    ANTEGRE = "1"
    MENSIES = "2"
    ENTRESEISYUNO = "3"
    MASUNO = "4"
    TIEM_PRIMER_EMPLE_OPTIONS = (
        (ANTEGRE, 'Antes de Egresar'),
        (MENSIES, 'Menos de seis meses'),
        (ENTRESEISYUNO, 'Entre seis meses y un año'),
        (MASUNO, 'Mas de un año'),
    )
    tiem_primer_emple = models.CharField(max_length=2,
                                      choices=TIEM_PRIMER_EMPLE_OPTIONS)

    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    CALIDAD_DOCENTES_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    calidad_docentes = models.CharField(max_length=2,
                                      choices=CALIDAD_DOCENTES_OPTIONS)

    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    PLAN_ESTUDIOS_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    plan_estudios= models.CharField(max_length=2,
                                      choices=PLAN_ESTUDIOS_OPTIONS)


    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    OPORT_PPID_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    oport_ppid = models.CharField(max_length=2,
                                      choices=OPORT_PPID_OPTIONS)

    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    ENFASIS_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    enfasis = models.CharField(max_length=2,
                                      choices=ENFASIS_OPTIONS)


    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    INFRACEST_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    infracest = models.CharField(max_length=2,
                                      choices=INFRACEST_OPTIONS)


    MBN = "1"
    BN = "2"
    RG = "3"
    ML = "4"
    EXPRECPROF_OPTIONS = (
        (MBN, 'Muy Buena'),
        (BN, 'Buena'),
        (RG, 'Regular'),
        (ML, 'Mala'),
    )
    exprecprof = models.CharField(max_length=2,
                                      choices=EXPRECPROF_OPTIONS)

    MUYEFI = "1"
    EFI = "2"
    POCEFI = "3"
    DEFI = "4"
    EFICIENCIA_LAB_OPTIONS = (
        (MUYEFI, 'Muy Eficiente'),
        (EFI, 'Eficiente'),
        (POCEFI, 'Poco Eficiente'),
        (DEFI, 'Deficiente'),
    
    )
    eficiencia_lab = models.CharField(max_length=2,
                                      choices=EFICIENCIA_LAB_OPTIONS)

    EXCL = "1"
    BUENO = "2"
    REG = "3"
    MLO = "4"
    PSMO = "5"
    CAL_FORMACION_OPTIONS = (
        (EXCL, 'Excelente'),
        (BUENO, 'Bueno'),
        (REG, 'Regular'),
        (MLO, 'Malo'),
        (PSMO, 'Pesimo'),
    
    )
    cal_formacion = models.CharField(max_length=2,
                                      choices=CAL_FORMACION_OPTIONS)

    EXCL = "1"
    BUENO = "2"
    REG = "3"
    MLO = "4"
    PSMO = "5"
    UTIL_RESIDENCIA_OPTIONS = (
        (EXCL, 'Excelente'),
        (BUENO, 'Bueno'),
        (REG, 'Regular'),
        (MLO, 'Malo'),
        (PSMO, 'Pesimo'),
    
    )
    util_residencia = models.CharField(max_length=2,
                                      choices=UTIL_RESIDENCIA_OPTIONS)

    def __unicode__(self):
        return self.nombre


class DatosLaborales (models.Model):
    egresado = models.ForeignKey(PerfilEgresado)
    
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
        (OTROS, 'Otros'),
    )
    medio_obt_trabajo = models.CharField(max_length=2,
                                      choices=MEDIO_OBT_TRABAJO_OPTIONS,
                                      default=BOLTRABPLAN,
                                      blank=True)

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
        (OTROS, 'Otro'),
    )
    req_contratacion = models.CharField(max_length=2,
                                      choices=REQ_CONTR_OPTIONS,
                                      default=COMPLAB,
                                      blank=True)


    PRINVAL = "1"
    NINGUNOS = "2"
    OTROS = "3"
    ACTIT_HABIL_OPTIONS = (
        (PRINVAL, 'Principios Y Valores'),
        (NINGUNOS, 'Ningunos'),
        (OTROS, 'Otros'),
    
    )
    actit_habil = models.CharField(max_length=2,
                                      choices=ACTIT_HABIL_OPTIONS)


    INGLES = "1"
    FRANCES = "2"
    ALEMAN = "3"
    JAPONES = "4"
    OTROS = "5"
    IDIOMA_TRAB_OPTIONS = (
        (INGLES, 'Ingles'),
        (FRANCES, 'Frances'),
        (ALEMAN, 'Aleman'),
        (JAPONES, 'Japones'),
        (OTROS, 'Otros'),
    
    )
    idioma_trab = models.CharField(max_length=2,
                                      choices=IDIOMA_TRAB_OPTIONS)


    hablar = models.IntegerField()
    escribir = models.IntegerField()
    leer = models.IntegerField()
    escuchar = models.IntegerField()

    salario_min_diario = models.FloatField()


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
                                      default=MENOS1,
                                      blank=True)

    anio_ingr_laboral = models.DateField(null=True, blank=True )

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
                                      default=TEC,
                                      blank=True)

    relac_trab_form = models.IntegerField()

    BAS = "1"
    EVTL = "2"
    CONTRA = "3"
    OTROS = "4"
    COND_TRAB_OPTIONS = (
        (BAS, 'Base'),
        (EVTL, 'Eventual'),
        (CONTRA, 'Contratado'),
        (OTROS, 'Otros'),
    )
    cond_trab = models.CharField(max_length=2,
                                      choices=COND_TRAB_OPTIONS)


    SI_TC = "1"
    NO_TC = "2"
    
    TOMAR_CURSO_OPTIONS = (
        (SI_TC, 'Si'),
        (NO_TC, 'No'),
    
    )
    tomar_curso = models.CharField(max_length=2,
                                    default=SI_TC,
                                    choices=TOMAR_CURSO_OPTIONS)


    cuales_tc = models.CharField(max_length=50)

    SI_TP = "1"
    NO_TP= "2"
    
    TOMAR_POSGRADO_OPTIONS = (
        (SI_TP, 'Si'),
        (NO_TP, 'No'),
    
    )
    tomar_posgrado = models.CharField(max_length=2,
                                      choices=TOMAR_POSGRADO_OPTIONS)

    cual_tp = models.CharField(max_length=50)



    
    SI_OS = "1"
    NO_OS = "2"
    
    ORG_SOCIAL_OPTIONS = (
        (SI_OS, 'Si'),
        (NO_OS, 'No'),
    
    )
    org_social = models.CharField(max_length=2,
                                      choices=ORG_SOCIAL_OPTIONS)

    cuales_os = models.CharField(max_length=50)
    
    SI_OP = "1"
    NO_OP = "2"
    
    ORG_PROF_OPTIONS = (
        (SI_OP, 'Si'),
        (NO_OP, 'No'),
    
    )
    org_prof = models.CharField(max_length=2,
                                      choices=ORG_PROF_OPTIONS)

    cuales_op = models.CharField(max_length=50)

    SI_AE = "1"
    NO_AE= "2"
    
    ASOC_EGRESADOS_OPTIONS = (
        (SI_AE, 'Si'),
        (NO_AE, 'No'),
    
    )
    asoc_egresados = models.CharField(max_length=2,
                                      choices=ASOC_EGRESADOS_OPTIONS)



    comentarios = models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.medio_obt_trabajo

   
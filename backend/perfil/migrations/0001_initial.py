# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_carrera', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DatosLaborales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_control', models.CharField(max_length=9)),
                ('medio_obt_trabajo', models.CharField(default=b'1', max_length=2, blank=True, choices=[(b'1', b'Bolsa de Trabajo del Plantel'), (b'2', b'Contacto Personales'), (b'3', b'Residencias Profesionales'), (b'4', b'Medios Masivos de Comunicaci\xc3\xb3n'), (b'5', b'Otros')])),
                ('req_contratacion', models.CharField(default=b'1', max_length=2, blank=True, choices=[(b'1', b'Competencias Laborales'), (b'2', b'Titulo Profesional'), (b'3', b'Examen de Selecci\xc3\xb3n'), (b'4', b'Idioma Extranjero'), (b'5', b'Otro')])),
                ('actit_habil', models.CharField(max_length=2, choices=[(b'1', b'Principios Y Valores'), (b'2', b'Ningunos'), (b'3', b'Otros')])),
                ('idioma_trab', models.CharField(max_length=2, choices=[(b'1', b'Ingles'), (b'2', b'Frances'), (b'3', b'Aleman'), (b'4', b'Japones'), (b'5', b'Otros')])),
                ('hablar', models.IntegerField()),
                ('escribir', models.IntegerField()),
                ('leer', models.IntegerField()),
                ('escuchar', models.IntegerField()),
                ('salario_min_diario', models.FloatField()),
                ('ant_empleo', models.CharField(default=b'1', max_length=2, blank=True, choices=[(b'1', b'Menos de un a\xc3\xb1o'), (b'2', b'Un a\xc3\xb1o'), (b'3', b'Dos a\xc3\xb1os'), (b'4', b'Tres a\xc3\xb1os'), (b'5', b'Mas de Tres a\xc3\xb1os')])),
                ('anio_ingr_laboral', models.DateField(null=True, blank=True)),
                ('niv_jerarquico', models.CharField(default=b'1', max_length=2, blank=True, choices=[(b'1', b'T\xc3\xa9cnico'), (b'2', b'Supervisor'), (b'3', b'Jefe de \xc3\x81rea'), (b'4', b'Funcionario'), (b'5', b'Directivo'), (b'5', b'Empresario')])),
                ('relac_trab_form', models.IntegerField()),
                ('cond_trab', models.CharField(max_length=2, choices=[(b'1', b'Base'), (b'2', b'Eventual'), (b'3', b'Contratado'), (b'4', b'Otros')])),
                ('tomar_curso', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('cuales_tc', models.CharField(max_length=50)),
                ('tomar_posgrado', models.CharField(max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('cual_tp', models.CharField(max_length=50)),
                ('org_social', models.CharField(max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('cuales_os', models.CharField(max_length=50)),
                ('org_prof', models.CharField(max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('cuales_op', models.CharField(max_length=50)),
                ('asoc_egresados', models.CharField(max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('comentarios', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilEgresado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_registro', models.DateField(auto_now_add=True)),
                ('f_modificacion', models.DateField(auto_now=True)),
                ('nombre', models.CharField(max_length=30)),
                ('a_paterno', models.CharField(max_length=30)),
                ('a_materno', models.CharField(max_length=30)),
                ('num_control', models.CharField(max_length=9)),
                ('f_nacimiento', models.DateField(blank=True)),
                ('sexo', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('curp', models.CharField(max_length=19)),
                ('e_civil', models.CharField(default=b'S', max_length=2, choices=[(b'C', b'Casado(a)'), (b'S', b'Soltero(a)'), (b'D', b'Divorciado(a)'), (b'O', b'Otro')])),
                ('estado', models.CharField(max_length=50, choices=[(b'Aguascalientes', b'Aguascalientes'), (b'Baja California Norte', b'Baja California Norte'), (b'Baja California Sur', b'Baja California Sur'), (b'Campeche', b'Campeche'), (b'Chiapas', b'Chiapas'), (b'Chihuahua', b'Chihuahua'), (b'Coahuila', b'Coahuila'), (b'Colima', b'Colima'), (b'Distrito Federal', b'Distrito Federal'), (b'Durango', b'Durango'), (b'Estado de Mexico', b'Estado de Mexico'), (b'Guanajuato', b'Guanajuato'), (b'Guerrero', b'Guerrero'), (b'Hidalgo', b'Hidalgo'), (b'Jalisco', b'Jalisco'), (b'Michoacan', b'Michoacan'), (b'Morelos', b'Morelos'), (b'Nayarit', b'Nayarit'), (b'Nuevo Leon', b'Nuevo Leon'), (b'Oaxaca', b'Oaxaca'), (b'Puebla', b'Puebla'), (b'Queretaro', b'Queretaro'), (b'Quintana Roo', b'Quintana Roo'), (b'San Luis Potosi', b'San Luis Potosi'), (b'Sinaloa', b'Sinaloa'), (b'Sonora', b'Sonora'), (b'Tabasco', b'Tabasco'), (b'Tamaulipas', b'Tamaulipas'), (b'Tlaxcala', b'Tlaxcala'), (b'Veracruz', b'Veracruz'), (b'Yucatan', b'Yucatan'), (b'Zacatecas', b'Zacatecas')])),
                ('ciudad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254, blank=True)),
                ('mes_anio_egreso', models.DateField(blank=True)),
                ('tel_casa', models.CharField(max_length=15)),
                ('niv_ing', models.IntegerField()),
                ('otros_idms', models.CharField(max_length=100)),
                ('man_paq_comp', models.CharField(max_length=200)),
                ('titulado', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Si'), (b'0', b'No')])),
                ('ocupacion', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Trabaja'), (b'2', b'Estudia'), (b'3', b'Trabaja y Estudia'), (b'4', b'Ni Trabaja Ni Estudia')])),
                ('estudios_act', models.CharField(max_length=2, choices=[(b'1', b'Especialidad'), (b'2', b'Maestria'), (b'3', b'Idiomas'), (b'4', b'Otros')])),
                ('esp_intitucion', models.CharField(max_length=50)),
                ('tiem_primer_emple', models.CharField(max_length=2, choices=[(b'1', b'Antes de Egresar'), (b'2', b'Menos de seis meses'), (b'3', b'Entre seis meses y un a\xc3\xb1o'), (b'4', b'Mas de un a\xc3\xb1o')])),
                ('calidad_docentes', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('plan_estudios', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('oport_ppid', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('enfasis', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('infracest', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('exprecprof', models.CharField(max_length=2, choices=[(b'1', b'Muy Buena'), (b'2', b'Buena'), (b'3', b'Regular'), (b'4', b'Mala')])),
                ('eficiencia_lab', models.CharField(max_length=2, choices=[(b'1', b'Muy Eficiente'), (b'2', b'Eficiente'), (b'3', b'Poco Eficiente'), (b'4', b'Deficiente')])),
                ('cal_formacion', models.CharField(max_length=2, choices=[(b'1', b'Excelente'), (b'2', b'Bueno'), (b'3', b'Regular'), (b'4', b'Malo'), (b'5', b'Pesimo')])),
                ('util_residencia', models.CharField(max_length=2, choices=[(b'1', b'Excelente'), (b'2', b'Bueno'), (b'3', b'Regular'), (b'4', b'Malo'), (b'5', b'Pesimo')])),
                ('carrera', models.ForeignKey(to='perfil.Carreras')),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='datoslaborales',
            name='egresado',
            field=models.ForeignKey(to='perfil.PerfilEgresado'),
        ),
    ]

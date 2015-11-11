# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_carrera', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DatosLaborales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medio_obt_trabajo', models.CharField(default=b'1', max_length=2, null=True, blank=True, choices=[(b'1', b'Bolsa de Trabajo del Plantel'), (b'2', b'Contacto Personales'), (b'3', b'Residencias Profesionales'), (b'4', b'Medios Masivos de Comunicaci\xc3\xb3n'), (b'5', b'Otros')])),
                ('req_contratacion', models.CharField(default=b'1', max_length=2, null=True, blank=True, choices=[(b'1', b'Competencias Laborales'), (b'2', b'Titulo Profesional'), (b'3', b'Examen de Selecci\xc3\xb3n'), (b'4', b'Idioma Extranjero'), (b'5', b'Otro')])),
                ('ant_empleo', models.CharField(default=b'1', max_length=2, null=True, blank=True, choices=[(b'1', b'Menos de un a\xc3\xb1o'), (b'2', b'Un a\xc3\xb1o'), (b'3', b'Dos a\xc3\xb1os'), (b'4', b'Tres a\xc3\xb1os'), (b'5', b'Mas de Tres a\xc3\xb1os')])),
                ('anio_ingr_laboral', models.DateTimeField()),
                ('niv_jerarquico', models.CharField(default=b'1', max_length=2, null=True, blank=True, choices=[(b'1', b'T\xc3\xa9cnico'), (b'2', b'Supervisor'), (b'3', b'Jefe de \xc3\x81rea'), (b'4', b'Funcionario'), (b'5', b'Directivo'), (b'5', b'Empresario')])),
            ],
        ),
        migrations.CreateModel(
            name='PerfilEgresado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('a_paterno', models.CharField(max_length=30)),
                ('a_materno', models.CharField(max_length=30)),
                ('num_control', models.CharField(max_length=9, null=True, blank=True)),
                ('f_nacimiento', models.DateTimeField()),
                ('sexo', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('curp', models.CharField(max_length=19)),
                ('e_civil', models.CharField(default=b'S', max_length=2, choices=[(b'C', b'Casado(a)'), (b'S', b'Soltero(a)'), (b'D', b'Divorciado(a)'), (b'O', b'Otro')])),
                ('estado', models.CharField(max_length=30, choices=[(b'Aguascalientes', b'Aguascalientes'), (b'Baja California Norte', b'Baja California Norte'), (b'Baja California Sur', b'Baja California Sur'), (b'Campeche', b'Campeche'), (b'Chiapas', b'Chiapas'), (b'Chihuahua', b'Chihuahua'), (b'Coahuila', b'Coahuila'), (b'Colima', b'Colima'), (b'Distrito Federal', b'Distrito Federal'), (b'Durango', b'Durango'), (b'Estado de Mexico', b'Estado de Mexico'), (b'Guanajuato', b'Guanajuato'), (b'Guerrero', b'Guerrero'), (b'Hidalgo', b'Hidalgo'), (b'Jalisco', b'Jalisco'), (b'Michoacan', b'Michoacan'), (b'Morelos', b'Morelos'), (b'Nayarit', b'Nayarit'), (b'Nuevo Leon', b'Nuevo Leon'), (b'Oaxaca', b'Oaxaca'), (b'Puebla', b'Puebla'), (b'Queretaro', b'Queretaro'), (b'Quintana Roo', b'Quintana Roo'), (b'San Luis Potosi', b'San Luis Potosi'), (b'Sinaloa', b'Sinaloa'), (b'Sonora', b'Sonora'), (b'Tabasco', b'Tabasco'), (b'Tamaulipas', b'Tamaulipas'), (b'Tlaxcala', b'Tlaxcala'), (b'Veracruz', b'Veracruz'), (b'Yucatan', b'Yucatan'), (b'Zacatecas', b'Zacatecas')])),
                ('cuidad', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('especialidad', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=254, null=True, blank=True)),
                ('mes_anio_egreso', models.DateTimeField()),
                ('titulado', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Si'), (b'2', b'No')])),
                ('ocupacion', models.CharField(default=b'1', max_length=2, choices=[(b'1', b'Trabaja'), (b'2', b'Estudia'), (b'3', b'Trabaja y Estudia'), (b'4', b'Ni Trabaja Ni Estudia')])),
                ('carrera', models.ForeignKey(to='perfil.Carreras')),
                ('empresa', models.ForeignKey(blank=True, to='empresa.Empresa', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='datoslaborales',
            name='egresado',
            field=models.ForeignKey(to='perfil.PerfilEgresado'),
        ),
    ]

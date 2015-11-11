# -*- coding: utf-8 -*-
from perfil.models import Carreras


Bio = Carreras (nombre_carrera= 'Ing.Bioquimica')
Civ = Carreras (nombre_carrera ='Ing.Civil')
Elec = Carreras (nombre_carrera ='Ing. Electronica')
Inds = Carreras (nombre_carrera ='Ing. Industrial')
Mec = Carreras(nombre_carrera = 'Ing.Mecatronica')
Isc = Carreras(nombre_carrera = 'Ing. Sist. Computacionales')
Admon = Carreras(nombre_carrera = 'Lic. Administración')
Cntp = Carreras(nombre_carrera = 'Contaduría Pública')
ElcMec = Carreras(nombre_carrera = 'Ing. Electromecánica')
Gemp = Carreras(nombre_carrera = 'Ing. Gestión Empresarial')
Log = Carreras(nombre_carrera = 'Ing. Logistica')

Bio.save() 
Civ.save()  
Elec.save() 
Inds.save()  
Mec.save()
Isc.save()
Admon.save()
Cntp.save()
ElcMec.save()
Gemp.save()
Log.save()


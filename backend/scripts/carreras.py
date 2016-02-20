# -*- coding: utf-8 -*-
from perfil.models import Carreras


Bio = Carreras (id=1,nombre_carrera= 'Ing.Bioquimica')
Civ = Carreras (id=2,nombre_carrera ='Ing.Civil')
Elec = Carreras (id=3,nombre_carrera ='Ing. Electronica')
Inds = Carreras (id=4,nombre_carrera ='Ing. Industrial')
Mec = Carreras(id=5,nombre_carrera = 'Ing.Mecatronica')
Isc = Carreras(id=6,nombre_carrera = 'Ing. Sist. Computacionales')
Admon = Carreras(id=7,nombre_carrera = 'Lic. Administración')
Cntp = Carreras(id=8,nombre_carrera = 'Contaduría Pública')
ElcMec = Carreras(id=9,nombre_carrera = 'Ing. Electromecánica')
Gemp = Carreras(id=10,nombre_carrera = 'Ing. Gestión Empresarial')
Log = Carreras(id=11,nombre_carrera = 'Ing. Logistica')

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


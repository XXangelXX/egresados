# comandos basicos
====================================


### iniciar entorno virtual

nota: suponiendo que los entornos virtuales estan en /home/user/venv
1. $ source venv/django1.8/bin/activate
    django1.8)user@pc:~$ 

### Entrar ala carpeta del proyecto y correrlo

nota: suponiendo que los entornos virtuales estan en /home/user/proyectos/backend
1.-(django1.8)luisangel19@ubuntu:~/proyectos/egresados$ cd backend
2.-(django1.8)luisangel19@ubuntu:~/proyectos/egresados/backend$ 
3.-python manage.py runserver

### para respaldar base de datos de mysql

    1.- $ mysqldump --user=angel --password myproject >bd.sql
    nota: donde angel es el nombre del usuario de la base de datos y bd.sql es el nombre del archivo.

### para restaurar  bases de datos
1.- $ mysql --user=angel --password egresadostec_db < base_egresados4feb.sql




### queryset para graficas

python manage.py shell
from Egresados.models import EgresadoPerfil
# query para sacar todos los de sistemas del 2006
EgresadoPerfil.objects.filter(pub_date__year=2006r).filter(carrera="6")


###grafica general
grafica de egresados por año desde el 1985 a actualidad

PerfilEgresado.objects.filter(pub_date__year=2000)
PerfilEgresado.objects.filter(mes_anio_egreso__year=2011).count()

datae_anio=[]
for anio in range(1985,2015):
    datae_anio = PerfilEgresado.objects.filter(mes_anio_egreso__year=anio).count()

print datae_anio





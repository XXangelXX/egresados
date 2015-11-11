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

###
### documentacion

###crear una base de datos mysql
mysql -u root -p
CREATE DATABASE egresados_db CHARACTER SET UTF8;

+ si no tenemos un usuario lo creamos
CREATE USER angel@localhost IDENTIFIED BY 'root';
+ si ya lo tenemos nos saltamos este paso 
GRANT ALL PRIVILEGES ON egresados_db.* TO angel@localhost;

+ donde angel es el nombre de usuario y egresados_db es el nombre de la db 

FLUSH PRIVILEGES;
+ para cambios se vean reflejados

#cambiar base de datos

1.- seguir los pasos para crear una bd nueva
2.- borrar las carpetas de migrations
3.- cambiar el settings.py por la nueva base de datos 
4.- hacer el siguiente comando 
    python manage.py migrate --fake-initial
5.- crear nuevo superusuario 
    python manage.py createsuperuser
6.- subir las carreras de egresados/scrips/carreras.py 
    python manage.py shell

7.- subir por csv o excel los nuevos datos.

### para borrar todos los datos de una tabla
from empresa.models import Empresa
>>> p= Empresa.objects.all()
>>> p.delete()
>>> Empresa.objects.all()
[]

### orden en el que se tienen que subir los archivos
- carreras
- encargado
- empresa
-
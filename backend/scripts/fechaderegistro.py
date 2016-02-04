from django.utils import timezone
from perfil.models import PerfilEgresado
users = PerfilEgresado.objects.all()
fecha = timezone.now())
for user in users:
    q = user(f_registro=fecha)
    q.save()
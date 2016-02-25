from django.contrib.auth.models import User
users = User.objects.all()
passwd = '2016' 
for user in users:
    user.set_password(passwd)
    user.save()

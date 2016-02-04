from django.contrib.auth.models import User
users = User.objects.all()
paswd = '2016' 
for user in users:
    passwd = passwd + user.username[:-3]
    user.set_password(passwd)
    user.save()

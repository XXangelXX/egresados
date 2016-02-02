from django.contrib.auth.models import User
users = User.objects.all()

for user in users:
    user.set_password('2016')
    user.save()

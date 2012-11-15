from django.contrib.auth.models import User
from django.contrib.auth.models import Group

grp=Group.objects.get_by_natural_key('dosa')
user = User.objects.create_user(username='dosa',password='dosa')
user.is_active=True
pr=user.get_profile()
pr.userType=4
pr.save()
user.save()
user.groups.add(grp)

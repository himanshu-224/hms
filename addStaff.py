from django.contrib.auth.models import User
from django.contrib.auth.models import Group

grp=Group.objects.get_by_natural_key('staff')
user = User.objects.create_user(username='staff',password='staff')
user.is_active=True
pr=user.get_profile()
pr.userType=2
pr.save()
user.save()
user.groups.add(grp)

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

grp=Group.objects.get_by_natural_key('student')

for i in range(1,11):
	genUsername="user"+str(i)
	genEmail=genUsername+"@mailhost.com"
	genPassword="pass"
	user = User.objects.create_user(username=genUsername,email=genEmail,password=genPassword)
	user.is_active=True
	pr=user.get_profile()
	pr.userType=0
	pr.save()
	user.save()
	user.groups.add(grp)



from mainapp.models import Policy

for i in range (1,5):	
	p=Policy(statement="s"+str(i), status="APP")
	p.save()

for i in range (6,10):	
	p=Policy(statement = "s"+str(i-4), proposal="p"+str(i), status="PFC", requestedTo="DS")
	p.save()

for i in range (11,14):	
	p=Policy(statement = "s"+str(i-4), proposal="p", status="PFC", requestedTo="SS")
	p.save()

for i in range (15,18):	
	p=Policy(proposal="n"+str(i), status="NPR", requestedTo="DS")
	p.save()

for i in range (18,20):	
	p=Policy(proposal="n"+str(i), status="NPR", requestedTo="SS")
	p.save()



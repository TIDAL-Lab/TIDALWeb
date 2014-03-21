from django.shortcuts import render, get_object_or_404
from tidalweb.models import People, AffilPerson
 
from views import index

def people(request):
	peeps = People.objects.filter(viewable=True)

	#director = People.objects.filter(viewable=True, status = 'director')
	#faculty = People.objects.filter(viewable=True, status='faculty')
	#phd = People.objects.filter(viewable = True, status = 'phd')
	#masters = People.objects.filter(viewable = True, status = 'masters')
	#undergrad = People.objects.filter(viewable = True, status = 'undergrad')

	#affilDirector = AffilPerson.objects.filter(viewable=True, status = 'director')
	#affilFaculty = AffilPerson.objects.filter(viewable=True, status='faculty')
	#affilPhd = AffilPerson.objects.filter(viewable = True, status = 'phd')
	#affilMasters = AffilPerson.objects.filter(viewable = True, status = 'masters')
	#affilUndergrad = AffilPerson.objects.filter(viewable = True, status = 'undergrad')

	#return render(request, 'people/people.html', {'director': director, 'faculty':faculty, 'phd':phd, 'masters':masters,'undergrad':undergrad, 'affilDirector':affilDirector, 'affilFaculty':affilFaculty, 'affilPhd':affilPhd, 'affilMasters':affilMasters, 'affilUndergrad':affilUndergrad})
	return render(request, 'people/people.html', {'peeps': peeps})
	

def personal(request, slug):
	# get the Post object
	person = get_object_or_404(People, slug=slug)
	# now return the rendered template
	return render(request, 'people/personal.html', {'person': person})# Create your views here.

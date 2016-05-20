from django.shortcuts import render, render_to_response, get_object_or_404
from tidal.models import People, Post, Project, Publication, FrontImage


def index(request):
  projects = Project.objects.filter(viewable=True, active=True, exhibit=False)
  exhibits = Project.objects.filter(viewable=True, active=True, exhibit=True)
  frontimages = FrontImage.objects.filter(published = True)
  return render_to_response('index.html', {'exhibits' : exhibits, 'projects' : projects, 'frontimages' : frontimages})

def contact(request):
    return render_to_response('contact.html')

def news(request):
  posts = Post.objects.filter(published=True)
  return render_to_response('news.html', {'posts': posts})

def people(request):
   peeps = People.objects.filter(viewable=True)
   return render(request, 'people.html', {'peeps': peeps})  

def personal(request, slug):
   person = get_object_or_404(People, slug=slug)
   return render(request, 'personal.html', {'person' : person})

def projects(request):
   projects = Project.objects.filter(active=True)
   return render(request, 'projects.html', {'projects' : projects})

def pubs(request):
   publist = Publication.objects.filter(pubAffil = 'lab', viewable = True).order_by('-year', '-created')
   return render_to_response('publications.html', {'pubs' : publist})



def bat(request):
  return render_to_response('projects/bat.html')

def biomap(request):
  return render_to_response('projects/biomap.html')

def fishing(request):
  return render_to_response('projects/fishing.html')

def frogpond(request):
  return render_to_response('frogpond/intro.html')

def frogpondChallenge(request):
  challenge = int(request.get_full_path()[-1:]) # get the challenge number from the url path
  return render_to_response('frogpond/challenge.html', { 'challenge' : challenge })

def greenhomegames(request):
  return render_to_response('projects/greenhomegames.html')

def roberto(request):
  return render_to_response('projects/roberto.html')

def spark(request):
  return  render_to_response('projects/spark.html')

def strawbies(request):
  return render_to_response('projects/strawbies.html')




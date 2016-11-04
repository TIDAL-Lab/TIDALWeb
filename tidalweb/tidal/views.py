from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tidal.models import *
from tidal.serializers import *
import datetime

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

def energyMonsters(request):
  return render_to_response('projects/energymonsters.html')



@csrf_exempt
def energyMeter(request):
  if request.method == 'GET':
    meter = 100
    if 'meter' in request.GET.keys():
      meter = request.GET['meter']
    meters = GHGEnergyMeter.objects.filter(meter=meter).order_by('-timestamp')[:10]
    serializer = GHGEnergyMeterSerializer(meters, many=True)
    content = JSONRenderer().render(serializer.data)
    response = HttpResponse(content, content_type="application/json")
    response.__setitem__("Access-Control-Allow-Origin", "*")
    return response

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = GHGEnergyMeterSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return HttpResponse('{ "result" : "success" }', status=201, content_type="application/json")
    return HttpResponse(serializer.errors, status=400, content_type="application/json")

  else:
    return HttpResponse("Invalid request", status=500)

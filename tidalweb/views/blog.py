from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

#def index(request):
#  return render_to_response('teaching.html')
 
def bat(request):
  return render_to_response(
    'blog/bat.html', 
    { 
      'title' : 'Build-a-Tree: Evolution Puzzle Game',
      'author' : 'Michael Horn',
      'description' : 'Build-a-Tree evolution puzzle game',
      'photo_credit' : 'flickr: Luke Andrew Scowen. Some rights reserved.'
     },
    context_instance=RequestContext(request))

def fishing(request):
  return render_to_response('blog/fishing.html', 
    { 
      'title' : 'Fishing with Friends',
      'author' : 'Michael Horn',
      'description' : 'Fishing with Friends, a game about sustainable fishing.'
    },
    context_instance=RequestContext(request))

def strawbies(request):
  return render_to_response(
    'blog/strawbies.html', 
    { 
      'title' : 'Strawbies Tangible Programming',
      'author' : 'Felix Hu',
      'description' : 'Strawbies tangible programming game',
      'photo_credit' : 'flickr: Fried Dough. Some rights reserved.'
    },
    context_instance=RequestContext(request))

def spark(request):
  return render_to_response(
    'blog/spark.html', 
    { 
      'title' : 'Spark: Electrical Circuit Exhibit',
      'author' : 'Elham Beheshti',
      'description' : 'Spark electrical circuit learning environment',
      'photo_credit' : 'flickr: Steve Johnson. Some rights reserved.'
    },
    context_instance=RequestContext(request))

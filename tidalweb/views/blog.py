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
      'description' : 'Build-a-Tree evolution puzzle game'
     },
    context_instance=RequestContext(request))

def fishing(request):
  return render_to_response('blog/fishing.html', { 
    'title' : 'Fishing with Friends',
    'author' : 'Michael Horn',
    'description' : 'Fishing with Friends, a game about sustainable fishing.'},
    context_instance=RequestContext(request))

def strawbies(request):
  return render_to_response(
    'blog/strawbies.html', 
    { 
      'title' : 'Strawbies Tangible Programming',
      'author' : 'Felix Hu',
      'description' : 'Strawbies tangible programming game'
    },
    context_instance=RequestContext(request))

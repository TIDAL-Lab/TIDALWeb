from django.http import HttpResponse
from django.shortcuts import render, render_to_response

#def index(request):
#  return render_to_response('teaching.html')
 
def bat(request):
  return render_to_response('blog/bat.html', { 'title' : 'Build-a-Tree Game' })

def fishing(request):
  return render_to_response('blog/fishing.html', { 'title' : 'Fishing with Friends' })

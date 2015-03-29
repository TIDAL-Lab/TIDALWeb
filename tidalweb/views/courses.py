from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def index(request):
  return render_to_response('teaching.html')
 
def tidal(request):
  return render_to_response('courses/tidal.html')

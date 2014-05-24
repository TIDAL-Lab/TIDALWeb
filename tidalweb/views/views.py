from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from tidalweb.models import Project
from tidalweb.models import Post
from tidalweb.models import Partner
from tidalweb.models import FrontImage, FrontPageBlurb

def index(request):
	projects = Project.objects.filter(viewable=True, active = True)
	posts = Post.objects.filter(published=True)
	labs = Partner.objects.filter(affiliation = 'labs')
	depts = Partner.objects.filter(affiliation = 'depts')
	oustideLabs = Partner.objects.filter(affiliation = 'oustideLabs')
	orgs = Partner.objects.filter(affiliation ='orgs')
	frontimages = FrontImage.objects.filter(published = True)
	frontPageBlurb = FrontPageBlurb.objects.all
	return render_to_response('index.html', {'projects': projects, 'posts':posts,'labs': labs, 'depts': depts, 'oustideLabs': oustideLabs, 'orgs': orgs,'frontimages': frontimages, 'frontPageBlurb':frontPageBlurb})


def greenhomegames(request):
  return render_to_response('greenhomegames.html')

def roberto(request):
  return render_to_response('roberto.html')

def nettango(request):
  return render_to_response('nettango.html')


def teaching(request):
  return render_to_response('teaching.html')


# def publications(request):
#     return render_to_response('publications.html')

# def people(request):
#     return render_to_response('people.html')

# def portfolio(request):
# 	return render_to_response('portfolio.html')

# def blog(request):
#     return render_to_response('blog/blog.html')

def contact(request):
    return render_to_response('contact.html')


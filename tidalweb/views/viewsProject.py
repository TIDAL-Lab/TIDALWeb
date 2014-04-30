from django.shortcuts import render, get_object_or_404
from tidalweb.models import Project, Photos, Tag

 
from views import index

def portfolio(request):
  # get the blog posts that are published
  curProjects = Project.objects.filter(viewable=True, active = True)
  pastProjects = Project.objects.filter(viewable=True, active = False)
  tags = Tag.objects.all
  # now return the rendered template
  return render(request, 'portfolio/portfolio.html', {'curProjects': curProjects, 'pastProjects': pastProjects, 'tags' : tags})
	
def project(request, slug):
	# get the Post object
	project = get_object_or_404(Project, slug=slug)
	# now return the rendered template
	return render(request, 'portfolio/project.html', {'project': project})# Create your views here.

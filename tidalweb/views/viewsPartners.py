from django.shortcuts import render, get_object_or_404
from tidalweb.models import Partner
 
from views import index

def partner(request):
    # get the blog posts that are published
    # pubs = Publication.objects.filter(published=True)
	labs = Partner.objects.filter(affiliation = 'labs')
	depts = Partner.objects.filter(affiliation = 'depts')
	oustideLabs = Partner.objects.filter(affiliation = 'oustideLabs')
	orgs = Partner.objects.filter(affiliation ='orgs')

    # now return the rendered template
	return render(request, 'index.html', {'labs': labs, 'depts': depts, 'oustideLabs': oustideLabs, 'orgs': orgs})

# def post(request, slug):
#     # get the Post object
#     post = get_object_or_404(Post, slug=slug)
#     # now return the rendered template
#     return render(request, 'blog/post.html', {'post': post})# Create your views here.

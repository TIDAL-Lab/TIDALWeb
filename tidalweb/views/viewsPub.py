from django.shortcuts import render, get_object_or_404
from tidalweb.models import Publication
 
from views import index

def pub(request):
    # get the blog posts that are published
    # pubs = Publication.objects.filter(published=True)
	journals = Publication.objects.filter(pubType = 'journal', pubAffil = 'lab', viewable = True).order_by('-year')
	books = Publication.objects.filter(pubType = 'book', pubAffil = 'lab', viewable = True).order_by('-year')
	refConfs = Publication.objects.filter(pubType = 'refConfs', pubAffil = 'lab', viewable = True).order_by('-year')
	presentations = Publication.objects.filter(pubType ='presentations', pubAffil = 'lab', viewable = True).order_by('-year')
	workshops = Publication.objects.filter(pubType = 'workshops', pubAffil = 'lab', viewable = True).order_by('-year')
	others = Publication.objects.filter(pubType = 'others', pubAffil = 'lab', viewable = True).order_by('-year')

	year = Publication.objects.filter(pubAffil = 'lab', viewable = True).order_by('-year')
    # now return the rendered template
	return render(request, 'publications.html', {'journals': journals, 'books': books, 'refConfs': refConfs, 'presentations': presentations, 'workshops': workshops, 'others': others, 'year':year})

# def post(request, slug):
#     # get the Post object
#     post = get_object_or_404(Post, slug=slug)
#     # now return the rendered template
#     return render(request, 'blog/post.html', {'post': post})# Create your views here.

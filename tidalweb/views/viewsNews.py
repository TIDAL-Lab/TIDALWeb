from django.shortcuts import render, get_object_or_404
from tidalweb.models import Post
 
from views import index

def news(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'news/news.html', {'posts': posts})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'news/post.html', {'post': post})# Create your views here.
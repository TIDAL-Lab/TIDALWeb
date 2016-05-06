from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib import staticfiles
from django.conf.urls.static import static
from django.views.generic import TemplateView
import views
import views.courses
import views.blog
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = 'index'),
    url(r'^index', views.index, name = 'index'),
    url(r'^publications', views.pubs, name = 'publications'),
    url(r'^people/$', views.people, name = 'people'),
    url(r'^portfolio/$', views.portfolio, name = 'portfolio'),
    url(r'^news/$', views.news, name = 'news'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^greenhomegames', views.greenhomegames, name = 'greenhomegames'),
    url(r'^roberto', views.roberto, name = 'roberto'),
    url(r'^biomap', views.biomap, name = 'biomap'),
    url(r'^reese', views.reese, name = 'reese'),
    url(r'^frogpond/$', views.frogpond, name = 'frogpond'),
    url(r'^frogpond/challenge[0-9]$', views.frogpondChallenge, name = 'frogpondChallenge'),
    url(r'^nettango', views.frogpond, name = 'nettango'),
    url(r'^teaching', views.teaching, name = 'teaching'),

    #---------------------------------------------------------------------
    # BLOG POSTS
    #---------------------------------------------------------------------
    url(r'^blog/bat', views.blog.bat, name = 'bat'),
    url(r'^blog/fishing', views.blog.fishing, name = 'fishing with friends'),
    url(r'^blog/strawbies', views.blog.strawbies, name = 'strawbies'),
    url(r'^blog/spark', views.blog.spark, name = 'spark'),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),

    #---------------------------------------------------------------------
    # COURSES 
    #---------------------------------------------------------------------
    url(r'^courses/$', views.courses.index, name = 'teaching'),
    url(r'^courses/eecs395/$', views.courses.tidal, name = 'tidal'),
    url(r'^courses/eecs495/$', views.courses.tidal, name = 'tidal'),
    url(r'^courses/ls451/$', views.courses.tidal, name = 'tidal'),
    url(r'^courses/tidal/$', views.courses.tidal, name = 'tidal'),

#   url(r'^$', 'blog.views.index'),
#   url(r'^$', 'people.views.index'),
#    url(r'^news/(?P<slug>[^/]+)/$', views.post),
    url(r'^people/(?P<slug>[\w\-]+)/$', views.personal, name = 'personal'),
    url(r'^portfolio/(?P<slug>[\w\-]+)/$', views.project),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),

) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

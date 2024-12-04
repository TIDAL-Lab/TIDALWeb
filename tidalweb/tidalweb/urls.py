from django.urls import include,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tidal import views

urlpatterns = [
   re_path(r'^admintidal/', admin.site.urls),
   re_path(r'^$', views.index, name = 'index'),
   re_path(r'^index/$', views.index, name = 'index'),
   re_path(r'^contact/$', views.contact, name = 'contact'),
   re_path(r'^news/$', views.news, name = 'news'),
   re_path(r'^people/$', views.people, name = 'people'),
   re_path(r'^people/(?P<slug>[\w\-]+)/$', views.personal, name = 'personal'),
   re_path(r'^projects/$', views.projects, name = 'projects'),
   re_path(r'^publications/$', views.pubs, name = 'publications'),
   re_path(r'^energymeter/$', views.energyMeter, name = 'energymeter'),
   re_path(r'^energymonsters/$', views.energyMonsters, name = 'energymonsters'),

   #-----------------------------------------------------------------
   # projects
   #-----------------------------------------------------------------
   re_path(r'^(?:blog/|projects/)?bat/$', views.bat, name = 'bat'),
   re_path(r'^(?:blog/|projects/)?biomap/$', views.biomap, name = 'biomap'),
   re_path(r'^(?:blog/|projects/)?fishing/$', views.fishing, name = 'fishing with friends'),
   re_path(r'^(?:blog/|projects/)?frogpond/$', views.frogpond, name = 'frogpond'),
   re_path(r'^(?:blog/|projects/)?frogpond/challenge[0-9]$', views.frogpondChallenge, name = 'frogpondChallenge'),
   re_path(r'^(?:blog/|projects/)?nettango/$', views.frogpond, name = 'nettango'),
   re_path(r'^(?:blog/|projects/)?nettango/challenge[0-9]$', views.frogpondChallenge, name = 'frogpondChallenge'),
   re_path(r'^(?:blog/|projects/)?greenhomegames/$', views.greenhomegames, name = 'greenhomegames'),
   re_path(r'^(?:blog/|projects/)?roberto/$', views.roberto, name = 'roberto'),
   re_path(r'^(?:blog/|projects/)?spark/$', views.spark, name = 'spark'),
   re_path(r'^(?:blog/|projects/)?strawbies/$', views.strawbies, name = 'strawbies'),

] 

#if settings.DEBUG is True:
#   urlpatterns +=+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + \
#           static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

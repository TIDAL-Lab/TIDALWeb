
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tidal import views

urlpatterns = [
   url(r'^admintidal/', admin.site.urls),
   url(r'^$', views.index, name = 'index'),
   url(r'^index/$', views.index, name = 'index'),
   url(r'^contact/$', views.contact, name = 'contact'),
   url(r'^news/$', views.news, name = 'news'),
   url(r'^people/$', views.people, name = 'people'),
   url(r'^people/(?P<slug>[\w\-]+)/$', views.personal, name = 'personal'),
   url(r'^projects/$', views.projects, name = 'projects'),
   url(r'^publications/$', views.pubs, name = 'publications'),
   url(r'^energymeter/$', views.energyMeter, name = 'energymeter'),
   url(r'^energymonsters/$', views.energyMonsters, name = 'gnergymonsters'),

   #-----------------------------------------------------------------
   # projects
   #-----------------------------------------------------------------
   url(r'^(?:blog/|projects/)?bat/$', views.bat, name = 'bat'),
   url(r'^(?:blog/|projects/)?biomap/$', views.biomap, name = 'biomap'),
   url(r'^(?:blog/|projects/)?fishing/$', views.fishing, name = 'fishing with friends'),
   url(r'^(?:blog/|projects/)?frogpond/$', views.frogpond, name = 'frogpond'),
   url(r'^(?:blog/|projects/)?frogpond/challenge[0-9]$', views.frogpondChallenge, name = 'frogpondChallenge'),
   url(r'^(?:blog/|projects/)?greenhomegames/$', views.greenhomegames, name = 'greenhomegames'),
   url(r'^(?:blog/|projects/)?nettango/$', views.frogpond, name = 'nettango'),
   url(r'^(?:blog/|projects/)?roberto/$', views.roberto, name = 'roberto'),
   url(r'^(?:blog/|projects/)?spark/$', views.spark, name = 'spark'),
   url(r'^(?:blog/|projects/)?strawbies/$', views.strawbies, name = 'strawbies'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

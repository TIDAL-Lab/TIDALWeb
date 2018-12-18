from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField

# People
class People(models.Model):
   name = models.CharField(max_length=255)
   title = models.CharField(max_length = 255)
   program = models.CharField(max_length = 255, blank = True)
   status = models.CharField(max_length = 255)
   biography = models.TextField()
   website = models.URLField(blank = True)
   linkedin = models.URLField(blank = True)
   photo = models.ImageField(upload_to = 'images/people/')
   cropping = ImageRatioField('photo', '300x300')
   cv = models.FileField(upload_to = 'files/cv/', blank = True)
   emailuser = models.CharField(max_length = 255)
   emaildomain = models.CharField(max_length = 255)
   slug = models.SlugField(unique=True, max_length=255)
   viewable = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   vieworder = models.IntegerField(default=100)

   class Meta:
      ordering = ['vieworder']
 
   def __unicode__(self):
      return u'%s' % self.name
 
   def get_absolute_url(self):
      return reverse('personal', args=[str(self.slug)])


# News
class Post(models.Model):
   title = models.CharField(max_length=255)
   author = models.CharField(max_length=255)
   slug = models.SlugField(unique=True, max_length=255)
   weblink = models.URLField(blank = True)
   description = models.CharField(max_length=255)
   content = models.TextField()
   published = models.BooleanField(default=True)
   pubdate = models.DateField(auto_now_add=True)
   created = models.DateTimeField(auto_now_add=True)
 
   class Meta:
      ordering = ['-pubdate']
 
   def __unicode__(self):
      return u'%s' % self.title
 
   def get_absolute_url(self):
      return reverse('tidal.views.post', args=[self.slug])


# Projects
class Project(models.Model):
   name = models.CharField(max_length=255)
   active = models.BooleanField(default=True)
   website = models.URLField(blank = True)
   about = models.TextField()
   grants = models.CharField(max_length=255, blank = True)
   videoURL = models.URLField(blank=True)
   thumb = models.ImageField(upload_to='images/projects/thumbs/')
   cropping = ImageRatioField('thumb', '172x172')
   projectCrop = ImageRatioField('thumb', '250x150')
   slug = models.SlugField(unique=True, max_length=255)
   exhibit = models.BooleanField(default=False)
   viewable = models.BooleanField(default=True)
   vieworder = models.IntegerField(default=100)
   created = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['vieworder']
 
   def __unicode__(self):
      return u'%s' % self.name
 
   def get_absolute_url(self):
      return reverse('tidal.views.project', args=[self.slug])


# Publications
class Publication(models.Model):
   authors = models.CharField(max_length=255)
   year = models.CharField(max_length=255)
   title = models.CharField(max_length=255)
   journal = models.CharField(max_length=255)
   pages = models.CharField(max_length=255, blank = True)
   award = models.CharField(max_length=255, blank=True)
   slug = models.SlugField(unique=True, max_length=255)
   viewable = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   localCopy = models.FileField(upload_to = 'files/pubs/', blank = True)
   weblink = models.URLField(blank = True)
   pubType = models.CharField(max_length = 255, choices = [('journal', 'Journal Articles'), ('book', 'Book Chapters'), ('refConfs', 'Refereed Conference Papers'), ('presentations', 'Presentations and Posters'), ('workshops', 'Workshop Papers'), ('others', 'Other Papers')])
   pubAffil = models.CharField(max_length = 255, choices = [('lab', 'TIDAL Lab'), ('personal', ('Personal'))])
   class Meta:
      ordering = ['-year']

   def __unicode__(self):
      return u'%s' % self.title


class FrontImage(models.Model):
   name = models.CharField(max_length=255)
   image = models.ImageField(upload_to = 'images/frontpage/')
   cropping = ImageRatioField('image', '910x350')
   slug = models.SlugField(unique=True, max_length=255)
   description = models.CharField(max_length=255, blank = True)
   published = models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   vieworder = models.IntegerField(default=100)

   class Meta:
      ordering = ['vieworder']
 
   def __unicode__(self):
      return u'%s' % self.name
 
   def get_absolute_url(self):
      return reverse('tidal.views.images', args=[self.slug])


class GHGEnergyMeter(models.Model):
   timestamp = models.DateTimeField(auto_now_add=True)
   meter = models.IntegerField(default=100)
   interval = models.IntegerField()
   Kt = models.FloatField(default=1.0)

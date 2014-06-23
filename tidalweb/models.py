from django.db import models
from django.core.urlresolvers import reverse
from image_cropping import ImageRatioField
from datetime import date

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
 
#    def get_absolute_url(self):
#        return reverse('viewsPub.pub', args=[self.slug])

class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.word

class Project(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    website = models.URLField(blank = True)
    about = models.TextField()
    videoURL = models.URLField(blank=True)
    thumb = models.ImageField(upload_to='images/projects/thumbs/')
    cropping = ImageRatioField('thumb', '172x172')
    projectCrop = ImageRatioField('thumb', '250x150')
    slug = models.SlugField(unique=True, max_length=255)
    viewable = models.BooleanField(default=True)
    vieworder = models.IntegerField(default=100)
    created = models.DateTimeField(auto_now_add=True)


    tags = models.ManyToManyField(Tag)

    def tagFilter(self):
        return Tag.objects.all

    def photoFilter(self):
        return Photos.objects.filter(myproject=self)


    def photoThumb(self):
        return list(Photos.objects.filter(myproject=self))[:1]

    def related(self):
        listofProjects =[]
        tags = self.tagFilter()
        for project in Project.objects.all():
            for tag in project.tagFilter():
                for myTag in tags:
                    if tag == myTag and project != self:
                        listofProjects.append(project)

        return listofProjects

    class Meta:
        ordering = ['vieworder']
 
    def __unicode__(self):
        return u'%s' % self.name
 
    def get_absolute_url(self):
        return reverse('tidalweb.views.project', args=[self.slug])


class Photos(models.Model):
    image = models.ImageField(upload_to='images/projects/')
    myproject = models.ForeignKey(Project)

class People(models.Model):
    name = models.CharField(max_length=255)
    netID = models.CharField(max_length = 255, blank = True)
    status = models.CharField(max_length = 255, choices = [('Director', 'Director'), ('Faculty', 'Faculty'), ('PhD Student', 'PhD Student'), ('Masters Student', 'Masters Student'), ('Undergraduate', 'Undergraduate Student'), ('Graphic Designer', 'Graphic Designer')])
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

    projects = models.ManyToManyField(Project, blank = True)

    publications = models.ManyToManyField(Publication, blank = True)

 
    class Meta:
        ordering = ['vieworder']
 
    def __unicode__(self):
        return u'%s' % self.name
 
    def get_absolute_url(self):
        return reverse('tidalweb.views.personal', args=[str(self.slug)])

class rInterests(models.Model):
    interests = models.CharField(max_length = 255)
    people = models.ForeignKey(People)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(People)
    slug = models.SlugField(unique=True, max_length=255)
    weblink = models.URLField(blank = True)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    pubdate = models.DateField(default=date.today())
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['-pubdate']
 
    def __unicode__(self):
        return u'%s' % self.title
 
    def get_absolute_url(self):
        return reverse('tidalweb.views.post', args=[self.slug])

class FrontImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/frontpage/')
    cropping = ImageRatioField('image', '940x350')
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
        return reverse('tidalweb.views.images', args=[self.slug])

class Partner(models.Model):
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    affiliation = models.CharField(max_length = 255, choices = [('labs', 'Northwestern Labs'), ('depts','Northwestern Departments'), ('oustideLabs', 'Outside Labs'), ('orgs', 'External Organizations')])
    logo = models.ImageField(upload_to = 'images/logos/', blank = True)
    url = models.URLField()
    slug = models.SlugField(unique=True, max_length=255)
    viewable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
 
    def __unicode__(self):
        return u'%s' % self.name
 
    def get_absolute_url(self):
        return reverse('tidalweb.views.partner', args=[self.slug])

class AffilPerson(models.Model):
    name = models.CharField(max_length=255)
    netID = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255, choices = [('director', 'Director'), ('faculty', 'Faculty'), ('phd', 'PhD Student'), ('masters', 'Masters Student'), ('undergrad', 'Undergraduate Student')])
    website = models.URLField()
    photo = models.ImageField(upload_to = 'images/people/', blank = True)
    slug = models.SlugField(unique=True, max_length=255)
    viewable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
 
    def __unicode__(self):
        return u'%s' % self.name
 
    def get_absolute_url(self):
        return reverse('tidalweb.views.personal', args=[self.slug])


class FrontPageBlurb(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)










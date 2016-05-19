from django.contrib import admin
from tidal.models import People, Post, Project, Publication, FrontImage

admin.site.register(People)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(FrontImage)


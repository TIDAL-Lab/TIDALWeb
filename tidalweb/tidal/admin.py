from django.contrib import admin
from tidal.models import People, Post, Project, Publication, FrontImage

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'pubdate')
    list_display_links = ('title',)

admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(FrontImage)


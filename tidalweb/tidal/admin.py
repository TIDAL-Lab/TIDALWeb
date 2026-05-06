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

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created')
    list_display_links = ('name', 'slug')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'authors')
    list_display_links = ('title',)

@admin.register(FrontImage)
class FrontImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'published')
    list_display_links = ('name', 'description')


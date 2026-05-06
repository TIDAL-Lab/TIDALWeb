from django.contrib import admin
from unfold.admin import ModelAdmin
from tidal.models import People, Post, Project, Publication, FrontImage

@admin.register(People)
class PeopleAdmin(ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'slug', 'pubdate')
    list_display_links = ('title',)

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'created')
    list_display_links = ('name', 'slug')


@admin.register(Publication)
class PublicationAdmin(ModelAdmin):
    list_display = ('title', 'year', 'authors')
    list_display_links = ('title',)

@admin.register(FrontImage)
class FrontImageAdmin(ModelAdmin):
    list_display = ('name', 'description', 'published')
    list_display_links = ('name', 'description')


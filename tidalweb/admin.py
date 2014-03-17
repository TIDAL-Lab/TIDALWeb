from django.contrib import admin
from models import FrontImage, Post, Partner, People, rInterests, AffilPerson, Project, Photos, Tag, Publication, FrontPageBlurb
from django.contrib.contenttypes import generic
from image_cropping import ImageCroppingMixin

class FrontAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # fields display on change list
    list_display = ['name',]
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['name',]
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("name",)}
 
admin.site.register(FrontImage, FrontAdmin)

 
class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
 
admin.site.register(Post, PostAdmin)

 
class PartAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name', 'affiliation', 'institution']
    # fields to filter the change list with
    list_filter = []
    # fields to search in change list
    search_fields = ['name', 'institution']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("name",)}
 
admin.site.register(Partner, PartAdmin)




class Interestsline(admin.TabularInline):
    model = rInterests


class PeopleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # fields display on change list
    list_display = ['name', 'status']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['name']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("name",)}

    inlines = [Interestsline]

class AffilAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name', 'status']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['name']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(People, PeopleAdmin)
admin.site.register(AffilPerson, AffilAdmin)



class Photosinline(admin.TabularInline):
    model = Photos
    extra = 1
    max_num = 5

# class Tagsinline(admin.StackedInline):
#     model = Tags
#     extra = 1
#     max_num = 1



class ProjectAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # fields display on change list
    list_display = ['name']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['name']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("name",)}

    inlines = [Photosinline]

class TagAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['word']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['word']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("word",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)

 
class PubAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'authors', 'year']
    # fields to filter the change list with
    list_filter = ['viewable', 'created']
    # fields to search in change list
    search_fields = ['title', 'authors', 'year']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
 
admin.site.register(Publication, PubAdmin)

class FrontPageBlurbAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'created']
    # fields to filter the change list with
    list_filter = ['created']
    # fields to search in change list
    search_fields = ['title']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
admin.site.register(FrontPageBlurb, FrontPageBlurbAdmin)

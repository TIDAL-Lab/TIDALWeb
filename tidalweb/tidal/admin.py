from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter, RangeDateTimeFilter
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from tidal.models import People, Post, Project, Publication, FrontImage

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(People)
class PeopleAdmin(ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'slug', 'pubdate')
    list_display_links = ('title',)
    list_filter = (
            ("pubdate", RangeDateFilter),
            ("created", RangeDateTimeFilter)
    )

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


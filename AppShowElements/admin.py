from django.contrib import admin
from .models import Kurs, Project

# Register your models here.
@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'icon','icon2']\

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'icon']
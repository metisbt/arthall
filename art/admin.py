from django.contrib import admin
from art.models import Category, Creation, Exhibition, Teaching, RegisterExhibition

@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'status', 'created_date', 'updated_date')
    list_filter = ('status','author')
    search_fields = ['title', 'content']

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('author' ,'name', 'proved', 'date', 'created_date', 'updated_date')
    list_filter = ('name','category', 'proved', 'date')
    search_fields = ['name', 'proved', 'date']

@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('author', 'name', 'subject', 'proved', 'date', 'created_date', 'updated_date')
    list_filter = ('name','category', 'proved', 'date')
    search_fields = ['name', 'proved', 'date']

@admin.register(RegisterExhibition)
class RegisterExhibitionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('author', 'name', 'created_date', 'updated_date')
    list_filter = ('name',)
    search_fields = ['name',]

admin.site.register(Category)


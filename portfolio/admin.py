from django.contrib import admin
from  .models import Category,Photo,Video

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image', 'created', 'updated']
    list_filter = ['created', 'updated', 'category']
    search_fields = ['name',]

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'video', 'created', 'updated']
    list_filter = ['created', 'updated', 'category']
    search_fields = ['name',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
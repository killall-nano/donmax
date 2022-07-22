from django.contrib import admin
from  .models import Category,Client,Photo,Video
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name',]

class ClientAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'cover_image', 'created', 'updated']
    list_filter = ['created', 'updated', 'category']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title',]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'image', 'created', 'updated']
    list_filter = ['created', 'updated', 'client']
    search_fields = ['name',]

class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'video', 'created', 'updated']
    list_filter = ['created', 'updated', 'client']
    search_fields = ['name',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)

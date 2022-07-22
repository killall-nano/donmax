from django.shortcuts import render, get_object_or_404
from .models import Photo, Video, Category

# Create your views here.
def portfolio(request, category_slug=None):
    category = None
    photos = Photo.objects.all()
    videos = Video.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        videos = videos.filter(category=category)
        photos = photos.filter(category=category)
    context={
        'category' : category,
        'categories' : categories,
        'photos' : photos,
        'videos' : videos,
        'nav_image' : 'cour3.png',
        'nav_title':'portfolio',
        'nav_description' : 'Pick up where you left off \
        Lesson 1: Welcome to the Full-Stack Web Developer Nanodegree Program'
    }
    return render(request, 'portfolio.html',context)

    
from django.shortcuts import render, get_object_or_404
from .models import Category, Client, Photo, Video
# Create your views here.
def clients(request,category_slug=None):
    category = None
    client = Client.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        client = Client.objects.filter(category=category)
    context={
        'category' : category,
        'categories' : categories,
        'clients' : client,
        'categories': categories,
        'nav_image' : 'cour5.jpg',
        'nav_title':'Clients',
        'nav_description' : 'Pick up where you left off \
        Lesson 1: Welcome to the Full-Stack Web Developer Nanodegree Program'
    }
    return render(request, 'client/clients.html', context)

def client_detail(request, id, slug):
    client = get_object_or_404(Client,id=id,slug=slug)
    photos = Photo.objects.filter(client=client)
    videos = Video.objects.filter(client=client)
    context = {
        'photos':photos,
        'videos':videos,
        'client':client
    }
    return render(request, 'client/client_detail.html', context)


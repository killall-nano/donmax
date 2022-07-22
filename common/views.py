from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def investments(request):
    context={
        'nav_image' : 'Background.png',
        'nav_title':'investments',
        'nav_description' : 'Pick up where you left off \
        Lesson 1: Welcome to the Full-Stack Web Developer Nanodegree Program'
    }
    return render(request, 'investment.html', context)

def about(request):
    context={
        'nav_image' : 'cour5.jpg',
        'nav_title':'about me',
        'nav_description' : 'Pick up where you left off \
        Lesson 1: Welcome to the Full-Stack Web Developer Nanodegree Program'
    }
    return render(request, 'about-me.html', context)

def contact(request):
    context={
        'nav_image' : 'cour6.jpg',
        'nav_title':'Contact Me',
        'nav_description' : 'Pick up where you left off \
        Lesson 1: Welcome to the Full-Stack Web Developer Nanodegree Program'
    }
    return render(request, 'contact.html', context)
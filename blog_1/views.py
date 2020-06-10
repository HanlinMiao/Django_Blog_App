from django.shortcuts import render
from . models import blogpost



def home(request):
    context = {
        'posts': blogpost.objects.all()
    }
    return render(request, 'blog_1/home.html', context)


def about(request):
    return render(request, 'blog_1/about.html', {'title': 'About'})


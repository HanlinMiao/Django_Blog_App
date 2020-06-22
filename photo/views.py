
from django.shortcuts import render, redirect, get_object_or_404
from .models import photo
from .forms import *
from django.http import HttpResponse

def home(request):
    context = {
        'photo': photo.objects.all()
    }
    return render(request, 'photo/gallery.html', context)

def gallery_view(request):
	if request.method == 'POST':
		form = PhotoUploadForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
			form = PhotoUploadForm()
	return render(request, 'photo/photo_form.html', {'form': form})

def success(request):
	return render(request, 'photo/photo_upload_success.html')


def display_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        photos = photo.objects.all()  
        return render(request, 'photo/display_images.html', {'photos' : photos})


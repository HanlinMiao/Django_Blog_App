
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import photo
from .forms import *
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
	photo_list = photo.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(photo_list, 4)
	try: 
		photos = paginator.page(page)
	except PageNotAnInteger:
		photos = paginator.page(1)
	except EmptyPage:
		photos = paginator.page(paginator.num_pages)

	return render(request, 'photo/display_images.html', {'photos': photos})

class PhotoCreateView(LoginRequiredMixin, CreateView):
	model = photo
	fields = ['title', 'image']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class UserPhotoListView(ListView):     
	model = photo
	template_name = 'photo/user_photo_list.html'
	context_object_name = 'photos'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return photo.objects.filter(author = user)

class UserPhotoDetailView(DetailView):
	model = photo
	

class UserPhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = photo
	fields = ['title', 'image', 'description']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		photo = self.get_object()
		if self.request.user == photo.author:
			return True
		return False
class UserPhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = photo
	success_url = "/photos"
	def test_func(self):
		photo = self.get_object()
		if self.request.user == photo.author:
			return True
		return False

def success(request):
	return render(request, 'photo/photo_upload_success.html')



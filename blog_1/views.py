from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import blogpost



def home(request):
    context = {
        'posts': blogpost.objects.all()
    }
    return render(request, 'blog_1/home.html', context)

def professional(request):
	return render(request,'blog_1/resume.html')

class PostListView(ListView):     #<app>/<model>_<viewtype>.html
	model = blogpost
	template_name = 'blog_1/home.html'
	context_object_name = 'posts'
	paginate_by = 5
	ordering = ['-date_posted']

class UserPostListView(ListView):     
	model = blogpost
	template_name = 'blog_1/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return blogpost.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = blogpost

class PostCreateView(LoginRequiredMixin, CreateView):
	model = blogpost
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = blogpost
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		blogpost = self.get_object()
		if self.request.user == blogpost.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = blogpost
	success_url = "/"
	def test_func(self):
		blogpost = self.get_object()
		if self.request.user == blogpost.author:
			return True
		return False

def about(request):
    return render(request, 'blog_1/about.html', {'title': 'About'})


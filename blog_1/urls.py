from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name ='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name ='user-posts'),
    path('blogpost/<int:pk>/', PostDetailView.as_view(), name ='blogpost-detail'),
    path('blogpost/new/', PostCreateView.as_view(), name ='blogpost-create'),
    path('blogpost/<int:pk>/update/', PostUpdateView.as_view(), name ='blogpost-update'),
    path('blogpost/<int:pk>/delete/', PostDeleteView.as_view(), name ='blogpost-delete'),
    path('about/',views.about, name ='blog-about'),
    

]

#<app>/<model>_<viewtype>.html
from django.urls import path
from . import views
from .views import success, PhotoCreateView, index

urlpatterns = [ 
	path('photos', index, name ='photo-gallery'),
	path('photos/upload', PhotoCreateView.as_view(), name ='photo-upload'),
	path('photos/upload/success', success, name = 'success'),
]
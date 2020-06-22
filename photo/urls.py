from django.urls import path
from . import views
from .views import *

urlpatterns = [ 
	path('photos', index, name ='photo-gallery'),
	path('photos/upload', gallery_view, name ='photo-upload'),
	path('photos/upload/success', success, name = 'success'),
]
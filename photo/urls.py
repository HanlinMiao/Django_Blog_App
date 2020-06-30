from django.urls import path
from . import views
from .views import success, PhotoCreateView, index, UserPhotoListView, UserPhotoDetailView, UserPhotoUpdateView, UserPhotoDeleteView

urlpatterns = [ 
	path('photos', index, name ='photo-gallery'),
	path('photos/upload', PhotoCreateView.as_view(), name ='photo-upload'),
	path('photos/<str:username>/', UserPhotoListView.as_view(), name = 'user-photo'),
	path('photos/<str:username>/<int:pk>/', UserPhotoDetailView.as_view(), name = 'photo-detail'),
	path('photos/<str:username>/<int:pk>/update/', UserPhotoUpdateView.as_view(), name = 'photo-update'),
	path('photos/<str:username>/<int:pk>/delete/', UserPhotoDeleteView.as_view(), name = 'photo-delete'),
	path('photos/upload/success', success, name = 'success'),

]
from django import forms
from .models import photo

class PhotoUploadForm(forms.ModelForm):
	class Meta:
		model = photo
		fields = ['title', 'image']
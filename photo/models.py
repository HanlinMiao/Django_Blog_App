from django.db import models
from PIL import Image


class photo(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to='photoGallery/')

	def __str__(self):
		return f'{self.title} photo'

	def save(self, *args, **kwargs):
		super(photo, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

# Create your models here.

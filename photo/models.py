from django.db import models
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class photo(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to='photoGallery/')
	author = models.ForeignKey(User, default = '0', on_delete = models.CASCADE, related_name = "authortophoto")
	description = models.TextField(max_length = 100, default = "DESCRIPTION")
	liked = models.ManyToManyField(User, default = None, blank= True, related_name = "usertophoto")
	
	def __str__(self):
		return f'{self.title} photo'

	def save(self, *args, **kwargs):
		super(photo, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
	def get_absolute_url(self):
		return reverse('success')
	@property
	def num_likes(self):
		return self.liked.all().count()
	
LIKE_CHOICES = (
 ('Like', 'Like'),
 ('Unlike', 'Unlike'),

)
class Like(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	photo = models.ForeignKey(photo, on_delete = models.CASCADE)
	value = models.CharField(choices = LIKE_CHOICES, default = "Like", max_length = 10)

	def __str__(self):
		return str(self.photo)
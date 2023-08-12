from django.db import models
import datetime

# Create your models here.
class Artist(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	profile_picture = models.ImageField(upload_to="cover_images/", default="cover_images/default_profile_picture.jpg",  null=False, blank=True)

	def __str__(self):
		return self.first_name+" "+self.last_name
	
class Event(models.Model):
	title = models.CharField(max_length=100)	
	description = models.TextField(null=True, blank=True)
	cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	author = models.ForeignKey(Artist, on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today , null=False, blank=True)
	image1 = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	image2 = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	image3 = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	
	def __str__(self):
		return self.title
	
class Article(models.Model):
	title = models.CharField(max_length=100)	
	content = models.TextField(null=True, blank=True)
	cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	author = models.ForeignKey(Artist, on_delete=models.CASCADE)
	image1 = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	image2 = models.ImageField(upload_to="cover_images/", null=True, blank=True)
	image3 = models.ImageField(upload_to="cover_images/", null=True, blank=True)

	def __str__(self):
		return self.title
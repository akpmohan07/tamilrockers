from django.db import models
# Create your models here.
class movie(models.Model):
	name = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	year = models.DateField()
	poster = models.ImageField(upload_to='media')
	def __str__(self):
		return self.name


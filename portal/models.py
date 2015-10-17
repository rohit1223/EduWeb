from django.db import models

class Question(models.Model):
	"""
	Description: Model Description
	"""
	question = models.CharField(max_length=200, unique=True)
	keywords = models.CharField(max_length=200, unique=True)
	def __unicode__(self):
		return self.question
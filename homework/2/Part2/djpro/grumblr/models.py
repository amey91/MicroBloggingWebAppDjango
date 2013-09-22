from django.db import models
from django.contrib.auth.models import User


class Grumblr(models.Model):
	user=models.ForeignKey(User)
	grumbl=models.CharField(max_length=1000)
	
		

	def __unicode__(self):
		return self.grumbl
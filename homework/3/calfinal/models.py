from django.db import models

# This application has no data models.
class cal(models.Model):
	ans = models.IntegerField()
	op = models.CharField(max_length=1)
	
	def __unicode__(self):
		return "cal"
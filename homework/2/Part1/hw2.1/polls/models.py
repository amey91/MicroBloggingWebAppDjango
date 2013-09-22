from django.db import models
from django.utils import timezone
# Create your models here.
		
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
	# ...
    def __unicode__(self): 
        return self.question
	# ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	# ...
    def __unicode__(self): 
        return self.choice_text

class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length =100)
	#..
	def __unicode__(self):
		return self.username
	




		
		
		
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from test.test_imageop import MAX_LEN


class Grumblr(models.Model):
	user=models.ForeignKey(User)
	grumbl=models.CharField(max_length=250)
	datetime=models.DateTimeField(auto_now_add='true')
		

	def __unicode__(self):
		return self.grumbl
	
class Follow(models.Model):
	info=models.CharField(max_length=100,default="default text for Follow")
	thefollower=models.ForeignKey(User,related_name="thefollower")
	thefollowed=models.ForeignKey(User,related_name="thefollowed")
	datetime=models.DateTimeField(auto_now_add='true')
		
	def __unicode__(self):
			return self.thefollower.username

class Comment(models.Model):
	grumblid=models.ForeignKey(Grumblr, related_name="grumblcomments")
	user=models.ForeignKey(User,related_name="commentby")
	comment=models.CharField(max_length=100)
	datetime=models.DateTimeField(auto_now_add='true')
	
	def __unicode__(self):
		return self.comment
	

class Block(models.Model):
	info=models.CharField(max_length=100,default="default text for Follow")
	theblocker=models.ForeignKey(User,related_name="theblocker")
	theblocked=models.ForeignKey(User,related_name="theblocked")
	datetime=models.DateTimeField(auto_now_add='true')
	
	def __unicode__(self):
		return self.theblocked.username
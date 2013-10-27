from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from test.test_imageop import MAX_LEN


class Grumblr(models.Model):
	user=models.ForeignKey(User, blank=False)
	grumbl=models.CharField(max_length=42, blank=False)
	datetime=models.DateTimeField(auto_now_add='true')
	dislikecounter=models.IntegerField(default=0)
	picture = models.ImageField(upload_to="pics", blank=True)	

	def __unicode__(self):
		return self.grumbl
	
	@staticmethod
	def get_entries(owner):
		return Grumblr.objects.filter(owner=owner).order_by(-id)
	
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
	
class Dislike(models.Model):
	datetime=models.DateTimeField(auto_now_add='true')
	user=models.ForeignKey(User,related_name="dislikeby")
	grumbl=models.ForeignKey(Grumblr,related_name="dislikedgrumbl")
	
	
	def __unicode__(self):
		return self.grumbl.user.username
	
	
class DislikeCount(models.Model):
	grumbl=models.ForeignKey(Grumblr,related_name="grumbldislikeccount")
	dislikecounter=models.IntegerField(default=0)
	def __unicode__(self):
		return self.grumbl.grumbl
	
	
class UserProfile(models.Model):
	user=models.ForeignKey(User, blank=False)
	picture = models.ImageField(upload_to="thesepics")
	
	def __unicode__(self):
		return self.user.username
	
	@staticmethod
	def get_entries(owner):
		return UserProfile.objects.get(user=owner)
	
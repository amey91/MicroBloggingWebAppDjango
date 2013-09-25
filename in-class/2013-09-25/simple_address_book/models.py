from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

class Entry(models.Model):
    owner = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address_1 = models.CharField(max_length=200, default="", blank=True)
    address_2 = models.CharField(max_length=200, default="", blank=True)
    city = models.CharField(max_length=200, default="", blank=True)
    state = models.CharField(max_length=200, default="", blank=True)
    zip = models.CharField(max_length=200, default="", blank=True)
    country = models.CharField(max_length=200, default="", blank=True)
    phone = models.CharField(max_length=200, default="", blank=True)
    
    def __unicode__(self):
	return self.first_name + " " + self.last_name

    @staticmethod
    def get_entries(owner):
        return Entry.objects.filter(owner=owner).order_by('last_name', 'first_name')

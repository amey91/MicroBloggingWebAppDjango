from django.db import models

SESSION_KEY = 'user_id'

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def __unicode__(self):
	return self.username

    # Based on django.contrib.auth.login
    def login(self, request):
        if SESSION_KEY in request.session:
            if request.session[SESSION_KEY] != self.pk:
                request.session.flush()
        else:
            request.session.cycle_key()
        request.session[SESSION_KEY] = self.pk
        if hasattr(request, 'user'):
            request.user = self

    # Authenticates a user based on a username and password, and 
    # returns the associated User instance
    @staticmethod
    def authenticate(username, password):
        return None

    # Creates a new user based on a username and password, and
    # returns the associated User instance
    @staticmethod
    def create_user(username, password):
        return None


class Item(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    def __unicode__(self):
	return self.text

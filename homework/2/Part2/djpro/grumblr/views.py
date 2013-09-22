from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


from grumblr.models import *

@login_required
def index(request):
    items = Grumblr.objects.filter(user=request.user)
    return render(request, 'grumblr/home.html', {'items' : items})

@login_required
def creategrumbl(request):
    errors = []
    if not 'grumbl' in request.POST or not request.POST['grumbl']:
        errors.append('You must enter an item to add.')
    else:
        new_item = Grumblr(grumbl=request.POST['grumbl'], user=request.user)
        new_item.save()
        errors.append("Grumbl created successfully!")

    items = Grumblr.objects.filter(user=request.user)
    context = {'items' : items, 'errors' : errors}
    return render(request, 'grumblr/mygrumblrs.html', context)


@login_required
def mygrumblrs(request):
    items = Grumblr.objects.filter(user=request.user)
    return render(request, 'grumblr/mygrumblrs.html', {'items' : items})
	

@login_required
def profile(request):
	return render(request, 'grumblr/profile.html', {})

@login_required	
def editprofile(request):
	return render(request, 'grumblr/editprofile.html', {})




	
def register(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'grumblr/register.html', context)

    errors = []
    context['errors'] = errors

    # Checks the validity of the form data
    if not 'username' in request.POST or not request.POST['username']:
	errors.append('Username is required.')
    else:
        # Save the username in the request context to re-fill the username
        # field in case the form has errrors
	context['username'] = request.POST['username']

    if not 'password1' in request.POST or not request.POST['password1']:
	errors.append('Password is required.')
    if not 'password2' in request.POST or not request.POST['password2']:
	errors.append('Confirm password is required.')

    if 'password1' in request.POST and 'password2' in request.POST \
       and request.POST['password1'] and request.POST['password2'] \
       and request.POST['password1'] != request.POST['password2']:
	errors.append('Passwords did not match.')

    if len(User.objects.filter(username = request.POST['username'])) > 0:
	errors.append('Username is already taken.')

    if errors:
        return render(request, 'grumblr/register.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'], \
                                        password=request.POST['password1'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(request, new_user)
    items = Grumblr.objects.all()
    context = {'items' : items, 'errors' : errors}
    return render(request, 'grumblr/home.html', context)
    

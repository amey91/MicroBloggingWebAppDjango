from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction

# Needed to manually create HttpResponses or raise an Http404 exception
from django.http import HttpResponse, Http404

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Helper function to guess a MIME type from a file name
from mimetypes import guess_type

from models import *
from forms import *


@login_required
def home(request):
    # Sets up list of just the logged-in user's (request.user's) address book
    context = {'entries':Entry.get_entries(request.user)}
    return render(request, 'simple-address-book/index.html', context)


@login_required
@transaction.commit_on_success
def add_entry(request):
    if request.method == "GET":
        context = {'form':EntryForm()}
        return render(request, 'simple-address-book/add-entry.html', context)
        
    new_entry = Entry(owner=request.user)
    form = EntryForm(request.POST, request.FILES, instance=new_entry)
    if not form.is_valid():
        context = {'form':form}
        return render(request, 'simple-address-book/add-entry.html', context)
   
    form.save()
    return redirect(reverse('home'))


@login_required
@transaction.commit_on_success
def edit_entry(request, id):
    entry_to_edit = get_object_or_404(Entry, owner=request.user, id=id)

    if request.method == 'GET':
        form = EntryForm(instance=entry_to_edit)  # Creates form from the 
        context = {'form':form, 'id':id}          # existing entry.
        return render(request, 'simple-address-book/edit-entry.html', context)

    # if method is POST, get form data to update the model
    form = EntryForm(request.POST, request.FILES, instance=entry_to_edit)

    if not form.is_valid():
        context = {'form':form, 'id':id} 
        return render(request, 'simple-address-book/edit-entry.html', context)

    form.save()
    return redirect(reverse('home'))


@login_required
def get_photo(request, id):
    entry = get_object_or_404(Entry, owner=request.user, id=id)
    if not entry.picture:
        raise Http404

    content_type = guess_type(entry.picture.name)
    return HttpResponse(entry.picture, content_type=content_type)


@transaction.commit_on_success
def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'simple-address-book/register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'simple-address-book/register.html', context)

    # If we get here the form data was valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'], \
                            password=form.cleaned_data['password1'])
    login(request, new_user)
    return redirect(reverse('home'))
    

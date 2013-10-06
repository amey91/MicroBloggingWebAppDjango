from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

class Item(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    def __unicode__(self):
	return self.text

def addItem(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
            return HttpResponseRedirect('/thanks/') 
    else:
        form = ContactForm() 

    return render(request, 'private-todo-list/index.html', {
        'form': form,
    })
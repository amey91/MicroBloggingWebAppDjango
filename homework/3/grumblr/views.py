from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from grumblr.models import *

def temp(request):
    items = Grumblr.objects.all()
    return render(request, 'grumblr/temp.html', {'items' : items})
    #b= Grumblr.objects.get(id=1)
    #b=b.mycomment_set.all()
    #return render(request, 'grumblr/temp.html',{'comments':b})

@login_required
def index(request):
    items = Grumblr.objects.all()
    return render(request, 'grumblr/home.html', {'items' : items})

@login_required
def allgrumblrs(request):
    items = Grumblr.objects.all()
    items = items.order_by('-id')
    b= Block.objects.filter(theblocker=request.user)
    for bl in b :
        items = items.exclude(user = bl.theblocked)
    return render(request, 'grumblr/allgrumblrs.html', {'items' : items})

@login_required
def mygrumblrs(request):
    items = Grumblr.objects.filter(user=request.user)
    items = items.order_by('-id')
    return render(request, 'grumblr/mygrumblrs.html', {'items' : items})


@login_required
def creategrumbl(request):
    errors = []
    if not 'grumbl' in request.POST or not request.POST['grumbl']:
        errors.append('You must enter an item to add.')
    else:
        new_item = Grumblr(grumbl=request.POST['grumbl'], user=request.user)
        new_item.save()
        Dislike
        errors.append("Grumbl created successfully!")
    items = Grumblr.objects.filter(user=request.user)
    items=items.order_by('-id')
    context = {'items' : items, 'errors' : errors}
    return render(request, 'grumblr/mygrumblrs.html', context)


@login_required
def profile(request):
    contextnew = {}
    uname=""
    if uname=="":
        uname=request.user
    
    u1 = User.objects.get(username=uname)
    contextnew['profile'] = u1
    u2 = Grumblr.objects.filter(user=request.user).count()
    if u2:
        contextnew['grumbls'] = u2
    return render(request, 'grumblr/profile.html', contextnew)

@login_required
def profile1(request,uname):
    contextnew = {}
    u1 = User.objects.get(username=uname)
    contextnew['profile'] = u1
    u2 = Grumblr.objects.filter(user=request.user).count()
    if u2:
        contextnew['grumbls'] = u2
    return render(request, 'grumblr/profile.html', contextnew)


@login_required	
def editprofile(request):
    contextnew = {}
    u1 = User.objects.get(username=request.user)
    contextnew['profile'] = u1
    u2 = Grumblr.objects.filter(user=request.user).count()
    if u2:
        contextnew['grumbls'] = u2
    return render(request, 'grumblr/editprofile.html', contextnew)


@login_required    	
def register(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'grumblr/register.html', context)

    errors = []
    context['errors'] = errors

    # Checks the validity of the form data
    if not 'username' in request.POST or not request.POST['username']:
	errors.append('Username is required.')
    if not 'lastname' in request.POST or not request.POST['lastname']:
        errors.append('Last Name is required.')
    if not 'firstname' in request.POST or not request.POST['firstname']:
        errors.append('First Name is required.')
    if not 'email' in request.POST or not request.POST['email']:
        errors.append('Email is required.')
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
    new_user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'], first_name=request.POST['firstname'],last_name=request.POST['lastname'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password1'])
    login(request, new_user)
    items = Grumblr.objects.all()
    context = {'items' : items, 'errors' : errors}
    return render(request, 'grumblr/home.html', context)

def main(request):
    return render(request, 'grumblr/main_template.html', {})
@login_required    
def searchgrumblrs(request):
    context = {}
    if request.POST['searchgrumbl']:
        a = request.POST['searchgrumbl']
        grumbls = Grumblr.objects.filter(grumbl__icontains=a)
        if grumbls.count == 0:
            context['errors']= "No Grumblrs found"
        context['grumbls'] = grumbls
        return render(request, "grumblr/search.html", context)
    else:
        context['errors'] = "Search Query contained null character."
        return render(request, "grumblr/search.html",context)
    

@login_required
def editprofilesubmit(request):
    context = {}
    u1 = User.objects.get(username=request.user)
    context['profile'] = u1
    if request.method == 'GET':
        return render(request, 'grumblr/editprofile.html', context)

    errors = []
    context['errors'] = errors

    # Checks the validity of the form data
    if not 'lastname' in request.POST or not request.POST['lastname']:
        errors.append('Last Name is required.')
    if not 'firstname' in request.POST or not request.POST['firstname']:
        errors.append('First Name is required.')
    if not 'email' in request.POST or not request.POST['email']:
        errors.append('Email is required.')
    context['username'] = request.POST['username']
    

    if errors:
        return render(request, 'grumblr/editprofile.html', context)

    # Creates the new user from the valid form data
    u1.first_name=request.POST['firstname']
    u1.last_name=request.POST['lastname']
    u1.email= request.POST['email'] 
    u1.save()
    context['success'] = "true"
    context['profile'] = u1
    return render(request,"grumblr/editprofile.html",context)


def changepassword(request):
    pass
    
@login_required    
def follow(request):
    f=Follow.objects.filter(thefollowed=request.user)
    u1 = request.user.username
    return render(request, "grumblr/myfollowers.html", {'followers':f, 'username': u1})

@login_required    
def findgrumblrs(request):
    u1=(Follow.objects.filter(thefollowed=request.user).values_list('thefollower',flat=True))
    u11=(User.objects.all().exclude(id__in = u1))
    u11=u11.exclude(id=request.user.id)
    h= Follow.objects.filter(thefollower=request.user)
    return render(request, "grumblr/findgrumblrs.html", {'followers':u11, 'username1': request.user, 'ihavefollowed':h})

@login_required    
def becomefollower(request):
    cont={}
    cont['errors']=[]
    if  request.method == "GET":
        return render(request,"grumblr/findgrumblrs.html", cont)
    try:
        u1= User.objects.get(username=request.POST['newuser'])
        f=Follow.objects.filter(thefollower=request.user).filter(thefollowed=u1)
        if f:
                cont['errors'].append("U have already followed this user")
                cont['username'] = request.user.username
                
        if request.user==u1:
                cont['errors'].append("U cannot follow yourself.")
                cont['username'] = request.user.username
                
        
        if not cont['errors']:
            f=Follow.objects.create(thefollower=request.user,thefollowed=u1)
            f.save()
    except ObjectDoesNotExist:
        cont['errors'].append("User does not exist.")
    cont['username'] = request.user.username
    u1=(Follow.objects.filter(thefollowed=request.user).values_list('thefollower',flat=True))
    u11=(User.objects.all().exclude(id__in = u1))
    u11=u11.exclude(id=request.user.id)
    h= Follow.objects.filter(thefollower=request.user)    
    cont['username1']= request.user
    cont['ihavefollowed']=h
    return render(request, "grumblr/findgrumblrs.html",cont)
    
#implement django forms here     
    
@login_required    
def add_comment(request,commentid):
    cont={}
    if request.POST['commenttext']=="":
        cont1={}
        comments = Comment.objects.filter(grumblid=commentid)
        g=Grumblr.objects.get(id=commentid)
        cont1['grumblr1']=g
        cont1['comments']=comments
        return render(request, "grumblr/temp2.html",cont1)
    #if request.method=="GET":
     #   return render(request, "grumblr/temp.html",cont)
    cont['var']=commentid
    g=Grumblr.objects.get(id=commentid)
    u=User.objects.get(username=request.user)
    c=Comment(grumblid=g, user=u, comment=request.POST['commenttext'])
    c.save()
    g=Grumblr.objects.all()
    for gr in g: 
        comments = Comment.objects.filter(grumblid=gr)
        for cd in comments:
                    cont['cd']= Comment.objects.filter(grumblid=cd.grumblid).count()
    cont['comments']=comments
    
    cont1={}
    comments = Comment.objects.filter(grumblid=commentid)
    cont1['commentcount'] = Comment.objects.filter(grumblid=commentid).count()
    g=Grumblr.objects.get(id=commentid)
    cont1['grumblr1']=g
    cont1['comments']=comments  
    return render(request, "grumblr/temp2.html",cont1)

@login_required    
def blockuser(request): 
    cont={}
    cont['errors']=[]
    ppl=Block.objects.filter(theblocker=request.user)
    cont['peopleihaveblocked']=ppl
    if  request.method == "GET":
        return render(request,"grumblr/blockuser.html", cont)
    try:
        u1= User.objects.get(username=request.POST['newuser'])
        f=Block.objects.filter(theblocker=request.user).filter(theblocked=u1)
        if f:
                cont['errors'].append("U have already blocked this user")
                cont['username'] = request.user.username
                return render(request, "grumblr/blockuser.html",cont)
        if request.user==u1:
                cont['errors'].append("U cannot block yourself.")
                cont['username'] = request.user.username
                return render(request, "grumblr/blockuser.html",cont)
        f=Block.objects.create(theblocker=request.user,theblocked=u1)
        y=Follow.objects.filter(thefollower=request.user,thefollowed=u1)
        if y: 
            y.delete()   
        f.save()
    except ObjectDoesNotExist:
        cont['errors'].append("User does not exist.")
    
    cont['username'] = request.user.username    
    return render(request, "grumblr/blockuser.html",cont)

    
@login_required
def dislikegrumbl(request,commentid):
    cont={}
    #if request.method=="GET":
     #   return render(request, "grumblr/temp.html",cont)
    cont['var']=commentid
    j=Grumblr.objects.get(id=commentid)
    u=Dislike.objects.filter(user=request.user).filter(grumbl=commentid)
    if (Grumblr.objects.filter(id=commentid).count() != 1):
            cont['errors'].append("Grumbl does not exist")
    
    if Dislike.objects.filter(user=request.user).filter(grumbl=commentid).count()>0:
           return render(request, "grumblr/temp.html",cont)
       #cont['errors'].append("Already dislied the Grumblr")
    
    if 'errors' in cont: 
        return render(request, "grumblr/temp.html",cont)
    
    d=Dislike(grumbl=j, user=request.user)
    d.save()
    j.dislikecounter=j.dislikecounter+1
    j.save()
    return render(request, "grumblr/temp.html",cont)

  
    
    
def temp2():
    pass
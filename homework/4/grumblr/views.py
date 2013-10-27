from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from grumblr.models import *
from grumblr.forms import *
from django.db import transaction 
from django.http import HttpResponse, Http404
from mimetypes import guess_type
from django.core.urlresolvers import reverse
from django.core.files import File
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import * 



@login_required
@transaction.commit_on_success
def temp(request):
    items = Grumblr.objects.all()
    return render(request, 'grumblr/temp.html', {'items' : items})
    # b= Grumblr.objects.get(id=1)
    # b=b.mycomment_set.all()
    # return render(request, 'grumblr/temp.html',{'comments':b})

@login_required
@transaction.commit_on_success
def index(request):
    items = Grumblr.objects.all()
    return render(request, 'grumblr/home.html', {'items' : items})

@login_required
def allgrumblrs(request):
    items = Grumblr.objects.all()
    items = items.order_by('-id')
    b = Block.objects.filter(theblocker=request.user)
    for bl in b :
        items = items.exclude(user=bl.theblocked)
    return render(request, 'grumblr/allgrumblrs.html', {'items' : items})

@login_required
def mygrumblrs(request):
    items = Grumblr.objects.filter(user=request.user)
    items = items.order_by('-id')
    return render(request, 'grumblr/mygrumblrs.html', {'items' : items})


@login_required
def creategrumblOLD(request):
    errors = []
    if not 'grumbl' in request.POST or not request.POST['grumbl']:
        errors.append('You must enter an item to add.')
    else:
        new_item = Grumblr(grumbl=request.POST['grumbl'], user=request.user)
        new_item.save()
        Dislike
        errors.append("Grumbl created successfully!")
    items = Grumblr.objects.filter(user=request.user)
    items = items.order_by('-id')
    context = {'items' : items, 'errors' : errors}
    return render(request, 'grumblr/mygrumblrs.html', context)

@login_required
def creategrumbloldnew(request):
    context = {}
    errors = []
    if request.method == 'GET':
        context['form'] = CreateGrumbls()
        return render(request, 'grumblr', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = CreateGrumbls(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'grumblr', context)

    # If we get here the form data was valid.  Register and login the user.
    new_item = Grumblr(grumbl=form.cleaned_data['grumbl'], user=request.user)
    new_item.save()
    errors.append("Grumbl created successfully!")
    items = Grumblr.objects.filter(user=request.user)
    items = items.order_by('-id')
    context = {'items' : items, 'errors' : errors}
    
    
    
    
    return render(request, 'grumblr/mygrumblrs.html', context)


@login_required
@transaction.commit_on_success
def creategrumbl(request):
    
    context = {}
    errors = []
    
    if len(request.POST['grumbl'])>42:
        context['grumbl_too_long']="true"
        return render(request, 'grumblr/home.html', context)
    
    if request.method == 'GET':
        form = GrumblrForm()  # Creates form from the 
        context = {'form':form, 'id':id}  # existing entry.
        return render(request, 'grumblr/home.html', context)
    
    new_entry = Grumblr(user=request.user)
    form = GrumblrForm(request.POST, request.FILES, instance=new_entry)

    if not form.is_valid():
        context = {'form':form, 'id':id} 
        return render(request, 'grumblr/home.html', context)

    

        
    form.save()
    errors.append("Grumbl created successfully!")
    
    ppl = Block.objects.filter(theblocker=request.user).values_list('theblocked', flat=True)
        
    items = Grumblr.objects.all().exclude(user__in = ppl)
    
    items = items.order_by('-id')
    context['items'] = items
    context['errors'] = errors
    context['form'] = form
    return render(request, 'grumblr/errorinform.html', context)
    


    

@login_required
def profile(request):
    contextnew = {}
    uname = ""
    if uname == "":
        uname = request.user
    
    u1 = User.objects.get(username=uname)
    contextnew['profile'] = u1
    u2 = Grumblr.objects.filter(user=request.user).count()
    if u2:
        contextnew['grumbls'] = u2
        
    # #set dp
    try:
        contextnew['profilepicture'] = UserProfile.objects.get(user=request.user)
        
    except ObjectDoesNotExist:
        contextnew['no_dp'] = "true"
    ####end set_dp
    return render(request, 'grumblr/profile.html', contextnew)





@login_required
def profile1(request, uname):
    if (uname == request.user.username) :
         return redirect('grumblr.views.profile')
        
    contextnew = {}
    u1 = User.objects.get(username=uname)
    contextnew['profile'] = u1
    
    # #set dp
    try:
        contextnew['profilepicture'] = UserProfile.objects.get(user=u1)
        
    except ObjectDoesNotExist:
        contextnew['no_dp'] = "true"
    ####end set_dp
    
    u2 = Grumblr.objects.filter(user=u1).count()
    if u2:
        contextnew['grumbls'] = u2
    return render(request, 'grumblr/others_profile.html', contextnew)


@login_required	
@transaction.commit_on_success
def editprofile(request):
    contextnew = {}
    u1 = User.objects.get(username=request.user)
    contextnew['profile'] = u1
    u2 = Grumblr.objects.filter(user=request.user).count()
    if u2:
        contextnew['grumbls'] = u2
        
    # #set dp
    try:
        contextnew['profilepicture'] = UserProfile.objects.get(user=request.user)
        
    except ObjectDoesNotExist:
        contextnew['no_dp'] = "true"
    ####end set_dp
    
    return render(request, 'grumblr/editprofile.html', contextnew)


@transaction.commit_on_success
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

    if len(User.objects.filter(username=request.POST['username'])) > 0:
	errors.append('Username is already taken.')
    

    if errors:
        return render(request, 'grumblr/register.html', context)

    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'], first_name=request.POST['firstname'], last_name=request.POST['lastname'])
    new_user.save()
    
    token = default_token_generator.make_token(new_user)
    email_body = """
Welcome to the Simple Address Book.  Please click the link below to
verify your email address and complete the registration of your account:

  http://%s%s
""" % (request.get_host(),
       reverse('confirm', args=(new_user.username, token)))
    send_mail(subject="Verify your email address",
              message=email_body,
              from_email="register+your+grumblr+account@grumblr.com",
              recipient_list=[new_user.email])
    
    
    
    
    
    # this creates the profile image into the model
    
    new_entry = UserProfile(user=request.user)
    form = UserProfileForm(request.POST, request.FILES, instance=new_entry)
    if not form.is_valid():
                
                context = {'form':form, 'id':id} 
                return render(request, 'grumblr/register_errors.html', context)
    form.save()
    context['profilepicture'] = UserProfile.objects.get(user=request.user)
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
    if not request.POST['searchgrumbl']:
        context['errors'] = "Search Query contained null character."
        return render(request, "grumblr/search.html", context)
    
    # #search term exists
    a = request.POST['searchgrumbl']
    ppl = Block.objects.filter(theblocker=request.user).values_list('theblocked', flat=True)
    
    grumbls = Grumblr.objects.filter(grumbl__icontains=a).exclude(user__in=ppl)
        
    if not grumbls :
        context['no_matching_grumbls'] = "true"
        print grumbls
    context['grumbls'] = grumbls
    print grumbls.count()
    return render(request, "grumblr/search.html", context)
    
    
        
    

@login_required
@transaction.commit_on_success
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
    u1.first_name = request.POST['firstname']
    u1.last_name = request.POST['lastname']
    u1.email = request.POST['email'] 
    u1.save()

    
           
    # display profile pic in the view using this
    try:
        if len(UserProfile.objects.filter(user=request.user)) > 0:
                context['dp_already_set'] = "true"
                context['profilepicture'] = UserProfile.objects.get(user=request.user)
        else:
            
            # #if profile picture doesnot exist in model 
            new_entry = UserProfile(user=request.user)
            form = UserProfileForm(request.POST, request.FILES, instance=new_entry)
            if not form.is_valid():
                # #if profile picture doesnot exist and form is not valid                
                context = {'form':form, 'id':id, 'everything_except_picture': "true"}
                context['profile'] = u1 
                return render(request, 'grumblr/terminal2.html', context)
            else:
                
                form.save()
            
            context['profilepicture'] = UserProfile.objects.get(user=request.user)
            
    except ObjectDoesNotExist:
        pass
    context['profilepicture'] = UserProfile.objects.get(user=request.user)
    context['success'] = "true"
    context['profile'] = u1
    return render(request, "grumblr/terminal1.html", context)


@login_required
@transaction.commit_on_success    
def follow(request):
    f = Follow.objects.filter(thefollowed=request.user)
    u1 = request.user.username
    return render(request, "grumblr/myfollowers.html", {'followers':f, 'username': u1})

@login_required    
def findgrumblrs(request):
    u1 = (Follow.objects.filter(thefollowed=request.user).values_list('thefollower', flat=True))
    u11 = (User.objects.all().exclude(id__in=u1))
    u11 = u11.exclude(id=request.user.id)
    h = Follow.objects.filter(thefollower=request.user)
    return render(request, "grumblr/findgrumblrs.html", {'followers':u11, 'username1': request.user, 'ihavefollowed':h})

@login_required    
@transaction.commit_on_success
def becomefollower(request):
    cont = {}
    cont['errors'] = []
    if  request.method == "GET":
        return render(request, "grumblr/findgrumblrs.html", cont)
    try:
        u1 = User.objects.get(username=request.POST['newuser'])
        f = Follow.objects.filter(thefollower=request.user).filter(thefollowed=u1)
        if f:
                cont['errors'].append("U have already followed this user")
                cont['username'] = request.user.username
                
        if request.user == u1:
                cont['errors'].append("U cannot follow yourself.")
                cont['username'] = request.user.username
                
        
        if not cont['errors']:
            f = Follow.objects.create(thefollower=request.user, thefollowed=u1)
            f.save()
    except ObjectDoesNotExist:
        cont['errors'].append("User does not exist.")
    cont['username'] = request.user.username
    u1 = (Follow.objects.filter(thefollowed=request.user).values_list('thefollower', flat=True))
    u11 = (User.objects.all().exclude(id__in=u1))
    u11 = u11.exclude(id=request.user.id)
    h = Follow.objects.filter(thefollower=request.user)    
    cont['username1'] = request.user
    cont['ihavefollowed'] = h
    u1 = (Follow.objects.filter(thefollowed=request.user).values_list('thefollower', flat=True))
    u11 = (User.objects.all().exclude(id__in=u1))
    u11 = u11.exclude(id=request.user.id)
    h = Follow.objects.filter(thefollower=request.user)
    cont['followers'] = u11
    cont['username1'] = request.user
    cont['ihavefollowed'] = h
    return render(request, "grumblr/findgrumblrs.html", cont)
    


@login_required    
@transaction.commit_on_success
def becomefollower1(request, uname):
    cont = {}
    cont['errors'] = []
    
    try:
        u1 = User.objects.get(username=uname)
        print u1
        f = Follow.objects.filter(thefollower=request.user).filter(thefollowed=u1)
        if f:
                cont['errors'].append("U have already followed this user")
                cont['username'] = request.user.username
                
        if request.user == u1:
                cont['errors'].append("U cannot follow yourself.")
                cont['username'] = request.user.username
                
        
        if not cont['errors']:
            f = Follow.objects.create(thefollower=request.user, thefollowed=u1)
            f.save()
    except ObjectDoesNotExist:
        cont['errors'].append("User does not exist.")
    cont['username'] = request.user.username
    u1 = (Follow.objects.filter(thefollowed=request.user).values_list('thefollower', flat=True))
    u11 = (User.objects.all().exclude(id__in=u1))
    u11 = u11.exclude(id=request.user.id)
    h = Follow.objects.filter(thefollower=request.user)    
    cont['username1'] = request.user
    cont['ihavefollowed'] = h
    u1 = (Follow.objects.filter(thefollowed=request.user).values_list('thefollower', flat=True))
    u11 = (User.objects.all().exclude(id__in=u1))
    u11 = u11.exclude(id=request.user.id)
    h = Follow.objects.filter(thefollower=request.user)
    cont['followers'] = u11
    cont['username1'] = request.user
    cont['ihavefollowed'] = h
    return render(request, "grumblr/findgrumblrs.html", cont)



# #implement djahngo forms here     
    
@login_required    
@transaction.commit_on_success
def add_comment(request, commentid):
    cont = {}
    if request.POST['commenttext'] == "":
        cont1 = {}
        comments = Comment.objects.filter(grumblid=commentid)
        g = Grumblr.objects.get(id=commentid)
        cont1['grumblr1'] = g
        cont1['comments'] = comments
        return render(request, "grumblr/comment_on_grimblr.html", cont1)
    # if request.method=="GET":
     #   return render(request, "grumblr/temp.html",cont)
    cont['var'] = commentid
    g = Grumblr.objects.get(id=commentid)
    u = User.objects.get(username=request.user)
    c = Comment(grumblid=g, user=u, comment=request.POST['commenttext'])
    c.save()
    g = Grumblr.objects.all()
    for gr in g: 
        comments = Comment.objects.filter(grumblid=gr)
        for cd in comments:
                    cont['cd'] = Comment.objects.filter(grumblid=cd.grumblid).count()
    cont['comments'] = comments
    
    cont1 = {}
    comments = Comment.objects.filter(grumblid=commentid)
    cont1['commentcount'] = Comment.objects.filter(grumblid=commentid).count()
    g = Grumblr.objects.get(id=commentid)
    cont1['grumblr1'] = g
    cont1['comments'] = comments  
    return render(request, "grumblr/comment_on_grimblr.html", cont1)

@login_required    
@transaction.commit_on_success
def blockuser(request): 
    cont = {}
    cont['errors'] = []
    ppl = Block.objects.filter(theblocker=request.user)
    cont['peopleihaveblocked'] = ppl
    if  request.method == "GET":
        return render(request, "grumblr/blockuser.html", cont)
    try:
        u1 = User.objects.get(username=request.POST['newuser'])
        f = Block.objects.filter(theblocker=request.user).filter(theblocked=u1)
        if f:
                cont['errors'].append("U have already blocked this user")
                cont['username'] = request.user.username
                return render(request, "grumblr/blockuser.html", cont)
        if request.user == u1:
                cont['errors'].append("U cannot block yourself.")
                cont['username'] = request.user.username
                return render(request, "grumblr/blockuser.html", cont)
        f = Block.objects.create(theblocker=request.user, theblocked=u1)
        y = Follow.objects.filter(thefollower=request.user, thefollowed=u1)
        if y: 
            y.delete()   
        f.save()
    except ObjectDoesNotExist:
        cont['errors'].append("User does not exist.")
    
    cont['username'] = request.user.username    
    return render(request, "grumblr/blockuser.html", cont)

    
@login_required
@transaction.commit_on_success
def dislikegrumbl(request, commentid):
    cont = {}
    # if request.method=="GET":
     #   return render(request, "grumblr/temp.html",cont)
    cont['var'] = commentid
    j = Grumblr.objects.get(id=commentid)
    u = Dislike.objects.filter(user=request.user).filter(grumbl=commentid)
    if (Grumblr.objects.filter(id=commentid).count() != 1):
            cont['errors'].append("Grumbl does not exist")
    
    if Dislike.objects.filter(user=request.user).filter(grumbl=commentid).count() > 0:
           items = Grumblr.objects.all()
           items = items.order_by('-id')
           b = Block.objects.filter(theblocker=request.user)
           for bl in b :
               items = items.exclude(user=bl.theblocked)
           return render(request, 'grumblr/allgrumblrs.html', {'items' : items})
           
       # cont['errors'].append("Already dislied the Grumblr")
    
    if 'errors' in cont: 
        items = Grumblr.objects.all()
        items = items.order_by('-id')
        b = Block.objects.filter(theblocker=request.user)
        for bl in b :
             items = items.exclude(user=bl.theblocked)
        return render(request, 'grumblr/allgrumblrs.html', {'items' : items})
    
    d = Dislike(grumbl=j, user=request.user)
    d.save()
    j.dislikecounter = j.dislikecounter + 1
    j.save()
    items = Grumblr.objects.all()
    items = items.order_by('-id')
    b = Block.objects.filter(theblocker=request.user)
    for bl in b :
        items = items.exclude(user=bl.theblocked)
    return render(request, 'grumblr/allgrumblrs.html', {'items' : items})
    
@login_required
def somebodysgrumbls(request, uname):
    u = User.objects.get(username=uname)
    items = Grumblr.objects.filter(user=u)
    items = items.order_by('-id')
    return render(request, 'grumblr/mygrumblrs.html', {'items' : items})  
    
    

@transaction.commit_on_success
def confirm_registration(request, username, token):
    user = get_object_or_404(User, username=username)

    # Send 404 error if token is invalid
    if not default_token_generator.check_token(user, token):
        raise Http404

    # Otherwise token was valid, activate the user.
    user.is_active = True
    user.save()
    return render(request, 'simple-address-book/confirmed.html', {})


@login_required
def get_photo(request, id):
    entry = get_object_or_404(Grumblr, id=id)
    print entry
    if not entry.picture:
        raise Http404
    content_type = guess_type(entry.picture.name)
    print content_type
    return HttpResponse(entry.picture, mimetype=content_type)


@login_required
def get_profile_photo(request, id):
    entry = get_object_or_404(UserProfile, id=id)
    
    if not entry.picture:
        raise Http404
    content_type = guess_type(entry.picture.name)
    
    return HttpResponse(entry.picture, mimetype=content_type)


@login_required
def xml_response(request,commentid):
        cont1 = {}
        comments = Comment.objects.filter(grumblid=commentid)
        g = Grumblr.objects.get(id=commentid)
        cont1['grumblr1'] = g
        cont1['comments'] = comments
        return render(request, 'grumblr/comments.xml', cont1, content_type='application/xml');
    
    

@login_required
def ppl_i_follow(request):
    u1 = (Follow.objects.filter(thefollower=request.user).values_list('thefollowed', flat=True))
    items=Grumblr.objects.filter(user__in = u1)
    b = Block.objects.filter(theblocker=request.user).values_list('theblocked',flat=True)
    items=items.exclude(user__in=b)
    return render(request, "grumblr/ppl_i_follow.html", {'items':items})

@login_required
def changepassword(request):
    context={}
    context['username']=User.objects.get(username=request.user)
    return render(request, "grumblr/changepassword.html", context)

@login_required
def changepasswordsubmit1(request):
    
    context={}
    errors=[]
    #//errors.append('Passwords did not match.')
    #//context['errors']=errors
    #return render(request, "grumblr/home.html", context)
    
    u=User.objects.get(username=request.user)
    if not 'ogipass' in request.POST or not request.POST['ogipass']:
        errors.append('Original is required.')
    if not 'newpass' in request.POST or not request.POST['newpass']:
        errors.append('New password is required.')
    if not 'newpass2' in request.POST or not request.POST['newpass2']:
        errors.append('confirm password is required.')
    
    if 'newpass' in request.POST and 'newpass2' in request.POST \
       and request.POST['newpass'] and request.POST['newpass2'] \
       and request.POST['newpass'] != request.POST['newpass2']:
            errors.append('Passwords did not match.')
    
    
    if errors:
        context['errors']=errors
        return render(request, "grumblr/changepassword.html", context)
    
    else:
        newpass=request.POST['newpass']
        u = User.objects.get(username__exact=request.user)
        u.set_password(newpass)
        u.save()
        context['success']="true"
    return render(request, "grumblr/changepassword.html", context)
    
    
        
    
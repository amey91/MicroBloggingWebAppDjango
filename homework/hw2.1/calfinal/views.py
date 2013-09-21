from django.shortcuts import render

from calfinal.models import *
# The action for the 'intro/hello-world' route.
def hello_world(request):
    # render takes: (1) the request,
    #               (2) the name of the view to generate, and
    #               (3) a dictionary of name-value pairs of data to be
    #                   available to the view.
    return render(request, 'calfinal/hello-world.html', {})


# The action for the 'intro/hello.html' route.
def hello(request):
	# Retrieves the name from the request if the 'name' parameter is present.
	name_to_greet = ''
	if '1' in request.GET:
		name_to_greet=request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='1'
		else: name_to_greet = name_to_greet + str(1)
		j=int(name_to_greet)
		
		'''name_to_greet = request.GET['1']
		c = cal.objects.get(id=1)
		c.ans=10076
		c.save()
		name_to_greet=10076
		if 'num1' in request.GET:
			if request.GET['num1']=="": 
				request.GET['num1']=0
			name_to_greet= int(request.GET['num1']) + request.GET['1']'''
	elif '2' in request.GET:
		name_to_greet = request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='2'
		else: name_to_greet = name_to_greet + str(2)
		
	elif '3' in request.GET:
		name_to_greet = request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='3'
		else: name_to_greet = name_to_greet + str(3)
		
	elif '4' in request.GET:
		name_to_greet = request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='4'
		else: name_to_greet = name_to_greet + str(4)
		
	elif '5' in request.GET:
		name_to_greet = request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='5'
		else: name_to_greet = name_to_greet + str(5)
		
		
	elif '6' in request.GET:
		name_to_greet = request.GET['num1']
		if name_to_greet == '0':
			name_to_greet='6'
		else: name_to_greet = name_to_greet + str(6)
		
	elif '7' in request.GET:
		name_to_greet = appendnum(request.GET['num1'],7)  # got tired of copy pasting and then took the long way around 
		
	elif '8' in request.GET:
		name_to_greet = appendnum(request.GET['num1'],8)
		
		
	elif '9' in request.GET:
		name_to_greet = appendnum(request.GET['num1'],9)
	elif '0' in request.GET:
		name_to_greet = appendnum(request.GET['num1'],0)
		
	elif '+' in request.GET:
		c=cal.objects.get(id=1)
		c.ans=request.GET['num1']
		c.op="+"
		c.save()		
		name_to_greet = 0
	# Makes the data available to the view as 'person_name', then renders the view
	
	elif '-' in request.GET:
		c=cal.objects.get(id=1)
		c.ans=request.GET['num1']
		c.op="-"
		c.save()		
		name_to_greet = 0
	
	elif 'x' in request.GET:
		c=cal.objects.get(id=1)
		c.ans=request.GET['num1']
		c.op="x"
		c.save()		
		name_to_greet = 0
	
	elif '/' in request.GET:
		c=cal.objects.get(id=1)
		c.ans=request.GET['num1']
		c.op="/"
		c.save()		
		name_to_greet = 0
	
	elif '=' in request.GET:
		c=cal.objects.get(id=1)
		if c.op=='':
			name_to_greet=request.GET['num1']
		if c.op== "+":
			name_to_greet=int(request.GET['num1'])+int(c.ans)
			c.ans=0
			c.op=""
			c.save()
		elif c.op=="/":
			name_to_greet=int(c.ans)/int(request.GET['num1'])
			c.ans=0
			c.op=""
			c.save()
		elif c.op=="-":
			name_to_greet=int(c.ans) - int(request.GET['num1'])
			c.ans=0
			c.op=""
			c.save()
		elif c.op=="x":
			name_to_greet=int(request.GET['num1'])*int(c.ans)
			c.ans=0
			c.op=""
			c.save()
			
			
	context = {'person_name':name_to_greet}
	return render(request, 'calfinal/greet.html', context)
	
def appendnum(a,b):
	if a == '0':
			return b
	else: 
		return a+str(b)
	

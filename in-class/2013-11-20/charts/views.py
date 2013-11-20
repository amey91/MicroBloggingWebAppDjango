from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

def bargraph(request):
    return render(request, 'charts/bargraph.html')

def svg(request):
	return render(request, 'charts/svg.html')

def svggraph(request):
	return render(request, 'charts/svggraph.html')

def svggraph2(request):
	return render(request, 'charts/svggraph2.html')
	
def githubgraph(request):
	return render(request, 'charts/githubgraph.html')
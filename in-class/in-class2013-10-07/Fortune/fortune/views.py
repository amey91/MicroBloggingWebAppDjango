from django.shortcuts import render
from fortunes import *

def home(request):
    fortune = get_fortune()
    return render(request, 'fortune/fortune.xml', {'fortune':fortune}, content_type='application/xml')

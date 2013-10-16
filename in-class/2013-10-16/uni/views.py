from django.shortcuts import render
from models import *

def home(request):
    return render(request, 'uni/index.html', {})

def get_students(request):
    first_name = request.GET.get('first_name', '')

    # The normal use of the ORM to get students by first name:
    #students = Student.objects.filter(first_name__exact=first_name)

    # The correct way to use raw SQL to get students by first name:
    #students = Student.objects.raw('select * from uni_student where first_name = %s', [first_name])

    # Gets students by first name, but is vulnerable to SQL injection attacks:
    students = Student.objects.raw('select * from uni_student where first_name = \'' + first_name + '\'')

    context = {'students':students}
    return render(request, 'uni/students.xml', context, content_type='application/xml')

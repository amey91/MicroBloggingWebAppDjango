from django.db import models

class Student(models.Model):
    andrew_id =  models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name

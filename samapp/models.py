from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50,default=True)
    branch = models.CharField(max_length=20)

    def __str__(self):
        self.name

class Language(models.Model):
    name = models.CharField(max_length=60,default=True)
    version = models.CharField(max_length=20,default=True)

    def __str__(self):
        self.name

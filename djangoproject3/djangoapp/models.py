from django.db import models

# Create your models here.

class Department(models.Model):
    group = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.group

class WebUserModel(models.Model):
    dept = models.ForeignKey(Department)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=50)

    def __str__(self):
        return self.dept

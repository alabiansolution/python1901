from django.db import models

# Create your models here.

class Topics(models.Model):
    top_name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topics)
    name = models.CharField(max_length=265, unique=True)
    url = models.CharField(max_length= 265, unique=True)

    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    webpage = models.ForeignKey(WebPage)
    date = models.DateField()

    def __str__(self):
        return self.date

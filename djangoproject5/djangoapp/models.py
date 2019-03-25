from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=60)
    def __str__(self):
        return self.cat_name


class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=60)
    post_content = models.CharField(max_length=100)
    def __str__(self):
        # return self.name + self.email + self.url + self.message
        return str(self.category)

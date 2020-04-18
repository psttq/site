from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    def __unicode__(self):
        return str(self.title, 'utf-8')
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.title, 'utf-8')

from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % self.category_name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1000)
    text = models.TextField()
    img_url = models.CharField(max_length=200, default=0)
    author = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    def __unicode__(self):
        return str(self.news_title, 'utf-8')

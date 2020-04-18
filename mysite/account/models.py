from django.db import models

# Create your models here.
class Usertype(models.Model):
    user_id = models.IntegerField(default=0)
    user_type = models.IntegerField(default=0)
    user_photo = models.CharField(max_length=2000, default="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Man_silhouette.svg/200px-Man_silhouette.svg.png")
    user_bio =  models.TextField(default="Здесь еще ничего нет! Расскажите о себе")

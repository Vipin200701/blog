from django.db import models

# Create your models here.
class new(models.Model):
    Title = models.CharField(max_length=20)
    Detail = models.TextField()
    #images = models.ImageField()
    
class Category(models.Model):
    Title = models.CharField(max_length=20)
    Category = models.CharField(max_length=200)
    Detail = models.TextField()
    images=models.FileField(upload_to="blogs/images/",max_length=250,null=True,default=None)
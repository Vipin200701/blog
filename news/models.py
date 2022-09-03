from pyexpat import model
from django.db import models
from tinymce.models import HTMLField
#from autoslug import AutoslugField
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=200)
    detail= HTMLField()
    images=models.FileField(upload_to="media/images/",max_length=250,null=True,default=None)
    #news_slug=AutoSlugField(populate_from='title',unique=True,null=True,Default=None)
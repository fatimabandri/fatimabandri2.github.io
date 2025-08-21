from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Aboutus(models.Model):
    title=models.CharField(max_length=100)
    about=HTMLField()
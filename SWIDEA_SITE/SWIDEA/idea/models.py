from django.db import models
from tkinter import CASCADE

# Create your models here.
class Devtool(models.Model):

    title=models.CharField(max_length=100)
    kind=models.CharField(max_length=100)
    content=models.TextField()
    def __str__(self):
        return self.title
    
class Idea(models.Model):

    choice_devtool=(('javascript','javascript'),('Python','Python'))

    title=models.CharField(max_length=100)
    image=models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content=models.TextField()
    like=models.IntegerField()
    devtool=models.ForeignKey(Devtool,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
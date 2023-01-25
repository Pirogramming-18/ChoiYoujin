from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='content')
    content_img = models.ImageField(verbose_name='img', upload_to='post_img')
    
    def __str__(self):
        return self.content

class PostLike(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(verbose_name='content', max_length=100)
    parentID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
    depth = models.IntegerField(verbose_name='depth')
    sequence = models.IntegerField(verbose_name='sequence')

    def __str__(self):
        return self.content

class CommentLike(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
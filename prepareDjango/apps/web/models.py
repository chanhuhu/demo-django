from datetime import datetime

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    login_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "{} : {} : {}".format(self.login_time, self.username, self.password)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return "{} {}".format(self.title, self.content)


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    tag = models.ManyToManyField(Tag)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.post.title)


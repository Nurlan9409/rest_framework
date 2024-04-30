from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True)

class Song(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

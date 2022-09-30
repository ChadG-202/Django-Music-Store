import os
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=256, null=True)
    lastname = models.CharField(max_length=256, null=True)
    email = models.EmailField(max_length=256, null=True)
    password = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Music(models.Model):
    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=256, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    digital = models.BooleanField(default=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    highResSong = models.FileField(upload_to='highResMusic/')
    song = models.FileField(upload_to='music/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def songURL(self):
        try:
            url = self.song.url
        except:
            url = ''
        return url

    @property
    def highResSongURL(self):
        try:
            url = self.highResSong.url
        except:
            url = ''
        return url

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    request_id = models.CharField(max_length=100, null=True)
    replied = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

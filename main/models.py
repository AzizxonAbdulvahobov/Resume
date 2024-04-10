from django.db import models

# Create your models here.
class AboutMe(models.Model):
    title = models.TextField()
    body = models.TextField()
    phone = models.CharField(max_length = 13)
    email = models.EmailField()
    website = models.URLField()
    img = models.ImageField(upload_to = 'about-me/')


class Education(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    mutahasis = models.CharField(max_length = 255)
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    detail = models.TextField()


class Skills(models.Model):
    name = models.CharField(max_length=255)
    foiz = models.SmallIntegerField()


class Expereiense(models.Model):
    start = models.IntegerField()
    finish = models.IntegerField(null =True , blank=True)
    company = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    detail = models.TextField()


class Profile(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)

class Partfolio(models.Model):
    img = models.ImageField(upload_to='portfolio/')
    name = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    

    
import sqlite3
from sqlite3 import Error
from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=255)
    videofile= models.FileField(upload_to='forms_video', null=True, verbose_name="")
    photo = models.FileField(upload_to='forms_video')
    def __str__(self):
        return self.name + ": " + str(self.videofile)
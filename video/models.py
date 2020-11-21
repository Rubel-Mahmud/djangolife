from django.db import models

class video(models.Model):
    title = models.CharField('title', max_length=200)
    embed = models.TextField('embed')

    def __str__(self):
        return self.title
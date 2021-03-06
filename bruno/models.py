from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.title



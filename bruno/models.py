from django.db import models
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from markdown import markdown

class Category(models.Model):
    #help_text gives hint
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title. Must be unique.')
    description = models.TextField()
    
    #inner class Meta to provide extra meta-information about a model
    class Meta:
        #specify plural name in admin page
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title
    
    #for a model to specify its own URL
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    #list of fields
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    #passing a callable
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    #html fields
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    #Metadata
    slug = models.SlugField(unique_for_date='pub_date', help_text='Suggested value automatically generated from title. Must be unique.')
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    #Categorization
    categories = models.ManyToManyField(Category)
    tags = TagField()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)

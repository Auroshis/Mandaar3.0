from django.db import models
from django.urls import reverse

class Noticeboard(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True) 
    Author = models.CharField(max_length=100,blank=False,default="No Author")
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    # add in target audience later

    def __str__(self):
        return str(self.title)

    #for slugs
    def get_absolute_url(self):
        return reverse('dashboard:notice_detail', kwargs={'slug': self.slug})

    #def snippet(self):
       # return self.body[:50] + '...'

    class Meta:
        verbose_name_plural = "Notices"

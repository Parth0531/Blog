from django.views.generic.dates import timezone_today
from mysite.settings import TIME_ZONE
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True,blank=False)
    slug = models.SlugField(max_length=200, unique=True,blank=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts',choices=None)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

        

    def get_absolute_url(self):
    #return reverse('article-detail', args=(str(self.id)) )
        return reverse('home')

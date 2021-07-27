from typing import Generic
from django.db.models import fields
from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from django.urls.base import reverse_lazy

# Create your views here.
from .models import Post
from django.views import generic

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields='__all__'

class UpdatePost(generic.UpdateView):
    model=Post
    template_name='edit_post.html'
    fields=['title','content','status']

class DeletePost(generic.DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')

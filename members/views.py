from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.

class UserRegisterView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

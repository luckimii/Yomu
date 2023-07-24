from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

class Homepage(ListView):
    model = Post
    template_name = 'homepage.html'

class Createstory(CreateView):
    model = Post
    template_name = 'createstory.html'
    form_class = PostForm
    success_url = reverse_lazy('homepage')

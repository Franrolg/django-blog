from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PrincipalView(ListView):
    model = Post
    template_name = "principal/index.html"
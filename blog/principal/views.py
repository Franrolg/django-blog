from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PrincipalView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "principal/componentes/lista-posts.html"
        return "principal/index.html"
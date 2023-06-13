from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    opciones = (
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
    )

    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="autor_post")
    contenido = models.TextField()
    estado = models.CharField(max_length=10, choices=opciones, default="borrador")

    creado = models.DateTimeField(auto_now_add=True, editable=False)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-creado",)

    def __str__(self):
        return f'{self.titulo} - {self.autor.get_full_name()}'
# Factory-Boy
import factory

# Modelos
from principal.models import Post
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "NombreTest"
    last_name = "ApellidoTest"
    username = "test"
    password = "test"
    is_superuser = True
    is_staff = True

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = "a"
    subtitulo = "b"
    slug = "c"
    autor = factory.SubFactory(UserFactory)
    contenido = "d"
    estado = "publicado"
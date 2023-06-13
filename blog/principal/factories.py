# Factory-Boy
import factory
from factory.faker import faker

# Modelos
from principal.models import Post
from django.contrib.auth.models import User

FAKE = faker.Faker()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    titulo = factory.Faker("sentence", nb_words=12)
    subtitulo = factory.Faker("sentence", nb_words=12)
    slug = factory.Faker("slug")
    autor = User.objects.get_or_create(username="admin")[0]

    @factory.lazy_attribute
    def contenido(self):
        x = ""
        for _ in range(0,5):
            x += "\n" + FAKE.paragraph(nb_sentences=30) + "\n"
        return x

    estado = "publicado"
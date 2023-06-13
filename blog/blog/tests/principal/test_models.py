import pytest

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(titulo="titulo de prueba")
        assert post.__str__() == f'titulo de prueba - {post.autor.get_full_name()}'
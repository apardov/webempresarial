from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Publicado', default=now)
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'

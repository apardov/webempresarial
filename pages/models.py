from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = CKEditor5Field(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "página"
        verbose_name_plural = 'páginas'
        ordering = ['title']

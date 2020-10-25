from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(
        'Nombre del Maestro', max_length=100, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)
    estado = models.BooleanField('Autor activo / No activo', default=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombres


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoría',
                              max_length=100, null=False, blank=False)
    fecha_creacion = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)
    estado = models.BooleanField(
        'Categoría activada / No activada', default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Título', max_length=150, null=False, blank=False)
    slug = models.SlugField('Slug', max_length=50,
                            null=False, blank=False, unique=True)
    descripcion = models.CharField(
        'Datos de Búsqueda', max_length=220, null=False, blank=False)
    contenido = RichTextUploadingField()
    volumen = models.CharField(
        'Volumen', max_length=100, null=False, blank=False)
    ubicacion = models.CharField(
        'Ubicación Física', max_length=100, null=False, blank=False)
    fecha_origen = models.DateField(
        'Fecha', auto_now=False, auto_now_add=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    fecha_publicacion = models.DateField(
        'Fecha de publicación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

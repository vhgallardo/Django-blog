from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

#MODELO CATEGORIAS
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

# MODELO ETIQUETAS
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name= 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']

    def __str__(self):
        return self.name

# MODELO POST
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    excerp = models.TextField(verbose_name='Bajada')
    #content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='post', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='get_posts',verbose_name='Categoría')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='get_posts', verbose_name='Author')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name= 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title

# MODELO ABOUT
class About(models.Model):
    description = models.CharField(max_length=350, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name= 'Acerca de'
        verbose_name_plural = 'Acerca de Nosotros'
        ordering = ['-created']

    def __str__(self):
        return self.description

# MODELO LINK
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key Link')
    name = models.CharField(max_length=120, verbose_name='Red Social')
    url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace')
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name= 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['name']

    def __str__(self):
        return self.name

# MODELO DEL COMENTARIO
class Comment(models.Model):
    comment = models.TextField(verbose_name='Comentario')
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.CharField(max_length=250, verbose_name='Correo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='get_posts',verbose_name='Posts')

    class Meta:
        verbose_name= 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-created']

    def __str__(self):
        return self.name

# MODELO MEWSLETTER

class Newsletter(models.Model):
    email = models.CharField(max_length=250, verbose_name='Correo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name= 'Boletín'
        verbose_name_plural = 'Boletines'
        ordering = ['created']

    def __str__(self):
        return self.email    
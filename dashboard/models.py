from django.db import models

# Create your models here.
class User(models.Model):
    password = models.CharField(max_length=200, verbose_name='Contraseña')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Último login')
    is_superuser = models.BooleanField(default=False, verbose_name='Super usuario')
    username = models.CharField(max_length=200, verbose_name='Usuario')
    last_name = models.CharField(max_length=200, verbose_name='Apellido')
    email = models.CharField(max_length=250, verbose_name='Correo')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    first_name = models.CharField(max_length=200, verbose_name='Nombre')

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['date_joined']

    def __str__(self):
        return self.username
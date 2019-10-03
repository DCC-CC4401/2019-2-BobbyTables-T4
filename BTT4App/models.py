from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.EmailField(default='Sin correo')


class PersonaNatural(Usuario):
    nombre = models.CharField(max_length=100, default='Sin nombre')
    apellido = models.CharField(max_length=100, default='Sin apellido')
    fotoDePerfil = models.ImageField(default='Sin foto de perfil')
    amigos = models.ManyToManyField('self')
    solicitudesPendientes = models.ManyToManyField('self')


class Administrador(Usuario):
    pass


class IActividad(models.Model):
    nombreDeActividad = models.CharField(max_length=100, default='Sin nombre')
    descripcion = models.CharField(max_length=100, default='Sin descripcion')
    categoria = models.CharField(max_length=100, default='Sin categoria')
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=True)


class ActividadTipo(IActividad):
    pass


class AbsActividad(IActividad):
    fechaYHora = models.DateTimeField(default='Sin fecha')
    duracion = models.IntegerField(default='Sin duracion')


class ActividadTiempoReal(AbsActividad):
    pass


class ActividadAPosteriori(AbsActividad):
    pass


from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


# Create your models here.

class PersonaNatural(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fotoDePerfil = models.ImageField(blank=True)
    amigos = models.ManyToManyField('self', blank=True)
    solicitudesPendientes = models.ManyToManyField('self', blank=True)

    def create_user(self, primerNombre, apellido, email, password):
        """
        Creates and saves a User with the given email and password.
        """

        if not primerNombre:
            raise ValueError('Usuarios deben tener un nombre.')
        if not apellido:
            raise ValueError('Usuarios deben tener un apellido.')
        if not email:
            raise ValueError('Usuarios deben tener un email.')
        if not password:
            raise ValueError('Usuarios deben tener una contraseña.')

        user = User(first_name=primerNombre, last_name=apellido, email=email, password=password)
        user.save()

        personaNatural = PersonaNatural(user=user)
        personaNatural.save()

        return personaNatural


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = User(email=email, password=password, is_superuser=True)
        user.save()

        admin = Administrador(user=user)
        admin.save()

        return admin


class IActividad(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=100, blank=False)

    def create_iActividad(self, nombre, descripcion, categoria):
        actividad = IActividad(nombre=nombre, descripcion=descripcion, categoria=categoria)
        actividad.save()
        return actividad


class ActividadTipo(IActividad):
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=False)


class AbsActividad(IActividad):
    fechaYHora = models.DateTimeField(default='Sin fecha')
    duracion = models.IntegerField(default='Sin duracion')

    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=True)

    def create_absActividad(self, fechaYHora, duracion):
        actividad = IActividad(fechaYHora=fechaYHora, duracion=duracion)
        actividad.save()
        return actividad


class ActividadTiempoReal(AbsActividad):
    pass


class ActividadAPosteriori(AbsActividad):
    pass

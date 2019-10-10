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

        persona_natural = PersonaNatural(user=user)
        persona_natural.save()

        return persona_natural

    def get_nombre(self):
        return self.user.first_name

    def get_apellido(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email

    def get_password(self):
        return self.user.password



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

    def get_email(self):
        return self.user.email

    def get_password(self):
        return self.user.password


class IActividad(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=100, blank=False)

    def create_iActividad(self, nombre, descripcion, categoria):
        actividad = IActividad(nombre=nombre, descripcion=descripcion, categoria=categoria)
        actividad.save()

        return actividad

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion

    def get_categoria(self):
        return self.categoria


class ActividadTipo(IActividad):
    fechaYHora = models.DateTimeField(default='Sin fecha', blank=True)
    duracion = models.IntegerField(default='Sin duracion', blank=True)
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=True)

    def create_ActividadTipo(self, nombre, descripcion, categoria):
        actividad_tipo = super(nombre, descripcion, categoria)
        actividad_tipo.save()

        return actividad_tipo

    def set_fecha_y_hora(self, fechaYHora):
        self.fechaYHora = fechaYHora

    def set_duracion(self, duracion):
        self.duracion = duracion

    def set_persona(self, persona):
        self.persona = persona

    def get_fechaYHora(self):
        return self.fechaYHora

    def get_duracion(self):
        return self.duracion

    def get_persona(self):
        return self.persona


class AbsActividad(IActividad):
    fechaYHora = models.DateTimeField(default='Sin fecha', blank=False)
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=False)

    def create_absActividad(self, nombre, descripcion, categoria, fechaYHora, persona):
        abs_actividad = IActividad(fechaYHora=fechaYHora, persona=persona)
        super(nombre, descripcion, categoria)
        abs_actividad.save()

        return abs_actividad

    def get_fechaYHora(self):
        return self.fechaYHora

    def get_persona(self):
        return self.persona


class ActividadTiempoReal(AbsActividad):
    duracion = models.IntegerField(default='Sin duracion', blank=True)

    def create_ActividadTiempoReal(self, nombre, descripcion, categoria, fechaYHora, persona):
        actividad_tiempo_real = super(nombre, descripcion, categoria, fechaYHora, persona)
        actividad_tiempo_real.save()

        return actividad_tiempo_real

    def set_duracion(self, duracion):
        self.duracion = duracion

    def get_duracion(self):
        return self.duracion


class ActividadAPosteriori(AbsActividad):
    duracion = models.IntegerField(default='Sin duracion', blank=False)

    def create_ActividadAPosteriori(self, nombre, descripcion, categoria, fechaYHora, duracion, persona):
        actividad_tipo = ActividadTipo(duracion=duracion)
        super(nombre, descripcion, categoria, fechaYHora, persona)
        actividad_tipo.save()

        return actividad_tipo

    def get_duracion(self):
        return self.duracion

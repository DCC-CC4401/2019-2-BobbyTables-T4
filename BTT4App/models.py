from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class PersonaNatural(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fotoDePerfil = models.ImageField(blank=True, default='profile_pics/turing.jpg', null=True, upload_to='profile_pics')

    amigos = models.ManyToManyField('self', blank=True)
    solicitudesPendientes = models.ManyToManyField('self', blank=True)

    def create_persona(self, primerNombre, apellido, email, password):
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
        user = User.objects.create_user(first_name=primerNombre, last_name=apellido, email=email, username=email,
                                        password=password)
        user.save()
        persona_natural = PersonaNatural(user=user)
        persona_natural.save()
        return persona_natural

    def get_nombre(self):
        # self.user.get_short_name()
        return self.user.first_name

    def get_apellido(self):
        return self.user.last_name

    def get_email(self):
        # self.user.get_username()
        return self.user.email

    def get_contrasena(self):
        return self.user.password

    def __str__(self):
        return f'{self.user.username} PersonaNatural'


class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def create_administrador(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = User.objects.create_superuser(email=email, username=email, password=password)
        user.save()
        admin = Administrador(user=user)
        admin.save()
        return admin

    def get_email(self):
        return self.user.email

    def get_password(self):
        return self.user.password


class IActividad(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.CharField(max_length=100, blank=False, null=True)
    categoria = models.CharField(max_length=100, blank=False, null=True)

    def create_i_actividad(self, nombre, descripcion, categoria):
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
    fecha_y_hora = models.DateTimeField(default='Sin fecha', blank=True, null=True)
    duracion = models.IntegerField(default='Sin duracion', blank=True, null=True)
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=True)

    def create_actividad_tipo(self, nombre, descripcion, categoria):
        actividad_tipo = super().create_i_actividad(nombre, descripcion, categoria)
        actividad_tipo.save()
        return actividad_tipo

    def set_fecha_y_hora(self, fecha_y_hora):
        self.fecha_y_hora = fecha_y_hora

    def set_duracion(self, duracion):
        self.duracion = duracion

    def set_persona(self, persona):
        self.persona = persona

    def get_fecha_y_hora(self):
        return self.fecha_y_hora

    def get_duracion(self):
        return self.duracion

    def get_persona(self):
        return self.persona


class Actividad(IActividad):
    fecha_y_hora = models.DateTimeField(default='Sin fecha', blank=False, null=True)
    persona = models.ForeignKey(PersonaNatural, models.SET_NULL, null=True, blank=False)
    duracion = models.IntegerField(default='Sin duracion', blank=True, null=True)

    def create_actividad(self, nombre, descripcion, categoria, fecha_y_hora, persona, tiempo):
        actividad = super().create_i_actividad(nombre, descripcion, categoria)
        actividad.fecha_y_hora = fecha_y_hora
        actividad.persona = persona
        actividad.tiempo = tiempo
        actividad.save()
        return actividad

    def get_fecha_y_hora(self):
        return self.fecha_y_hora

    def get_persona(self):
        return self.persona

    def set_duracion(self, duracion):
        self.duracion = duracion

    def get_duracion(self):
        return self.duracion

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo

    def get_tiempo(self):
        return self.tiempo

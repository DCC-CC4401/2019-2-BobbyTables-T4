# Generated by Django 2.2.5 on 2019-10-18 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaNatural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoDePerfil', models.ImageField(blank=True, null=True, upload_to='')),
                ('amigos', models.ManyToManyField(blank=True, related_name='_personanatural_amigos_+', to='BTT4App.PersonaNatural')),
                ('solicitudesPendientes', models.ManyToManyField(blank=True, related_name='_personanatural_solicitudesPendientes_+', to='BTT4App.PersonaNatural')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActividadTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('fecha_y_hora', models.DateTimeField(blank=True, default='Sin fecha', null=True)),
                ('duracion', models.IntegerField(blank=True, default='Sin duracion', null=True)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BTT4App.PersonaNatural')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('fecha_y_hora', models.DateTimeField(default='Sin fecha', null=True)),
                ('duracion', models.IntegerField(blank=True, default='Sin duracion', null=True)),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BTT4App.PersonaNatural')),
            ],
        ),
    ]

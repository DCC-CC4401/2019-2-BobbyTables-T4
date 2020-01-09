import unittest
from django.test import TestCase
from BTT4App.models import *

class test_models(TestCase):

    def setUp(self):
        self._user1 = User()
        self._user2 = User()
        self._userA = User()

        self._persona_natural_1 = PersonaNatural(user=self._user1)
        self._persona_natural_2 = PersonaNatural(user=self._user2)
        self._admin = Administrador(user=self._userA)

        # self._actividad_tipo = ActividadTipo()
        # self._actividad_tiempo_real = Actividad()
        # self._actividad_a_posteriori = Actividad()

        self._persona_natural_1.create_persona("nom1", "ape1", "cor1@gmail.com", "contra1")
        self._persona_natural_2.create_persona("nom2", "ape2", "cor2@gmail.com", "contra2")
        self._admin.create_administrador("admin@admin.admin", "admin")

        # self._actividad_tipo.create_actividad_tipo("estudiar", "estudiar mucho", "academico")
        #
        # self._actividad_tiempo_real.create_actividad("entrenar", "entrenar Voleibol", "deporte",
        #                                                        "2019.10.10 14:30", self._persona_natural_1, "real")
        # self._actividad_a_posteriori.create_actividad("jugar", "jugar Catan", "sacar la vuelta",
        #                                                          "2019.10.10 10:00", self._persona_natural_1, "posteriori")

    def test_gets(self):
        self.assertEqual(self._persona_natural_1.get_nombre(), "nom1")
        self.assertEqual(self._persona_natural_2.get_email(), "cor1@gmail.com")
        # self.assertEqual(self._persona_natural_2.user.get_short_name(), "nom2")
        # self.assertEqual(self._persona_natural_1.user.get_username(), "cor1@gmail.com")

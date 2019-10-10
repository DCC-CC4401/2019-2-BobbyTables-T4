import unittest
from django.test import TestCase
from BTT4App.models import *


# Create your tests here.


class test_models(TestCase):

    def setUp(self):
        self._persona_natural_1 = PersonaNatural()
        self._persona_natural_2 = PersonaNatural()
        self._admin = Administrador()
        self._actividad_tipo = ActividadTipo()
        self._actividad_tiempo_real = ActividadTiempoReal()
        self._actividad_a_posteriori = ActividadAPosteriori()

        self._persona_natural_1.create_user("nom1","ape1","cor1@gmail.com","contra1")
        self._persona_natural_2.create_user("nom2","ape2","cor2@gmail.com","contra2")

        self._admin.create_superuser("admin@gmail.com","admin1234")

        self._actividad_tipo.create_ActividadTipo("estudiar","estudiar mucho","academico")

        self._actividad_tiempo_real.create_ActividadTiempoReal("entrenar","entrenar Voleibol","deporte","2019.10.10 14:30",self._persona_natural_1)
        self._actividad_a_posteriori.create_ActividadAPosteriori("jugar","jugar Catan","sacar la vuelta","2019.10.10 10:00",60,self._persona_natural_1)


    def test_gets(self):
        self.assertTrue(self._persona_natural_1.get_nombre(),"nom1")



if __name__ == '__main__':
    unittest.main()


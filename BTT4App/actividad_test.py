from django.test import TestCase
from BTT4App.models import *

class test_models(TestCase):

    def setUp(self):

        self.actividad_tipo = ActividadTipo.create_actividad_tipo(ActividadTipo(), "estudiar", "estudiar mucho", "academico")

    def test_gets(self):

        self.assertEqual(self.actividad_tipo.get_nombre(), "estudiar")

from django.test import TestCase
from BTT4App.models import *

class test_models(TestCase):

    def setUp(self):

        self._persona_natural_1 = PersonaNatural.create_persona(self, "nom1", "ape1", "cor1@gmail.com", "contra1")
        self._persona_natural_2 = PersonaNatural.create_persona(self, "nom2", "ape2", "cor2@gmail.com", "contra2")

        self._admin = Administrador.create_administrador(self, "admin@admin.admin", "admin")

        self._actividad_tipo = ActividadTipo.create_actividad_tipo(self, "estudiar", "estudiar mucho", "academico")
        self._actividad_t = Actividad.create_actividad(self, "entrenar", "entrenar Voleibol", "deportes",
                                                       "2019/04/04 12:00:00", self._persona_natural_1, "real")
        self._actividad_p = Actividad.create_actividad(self, "jugar", "jugar Catan", "ocio", "2019/04/05 13:30:00",
                                                       self._persona_natural_2, "post")

    def test_gets(self):

        self.assertEqual(self._persona_natural_1.get_nombre(), "nom1")
        self.assertEqual(self._persona_natural_1.get_apellido(), "ape1")
        self.assertEqual(self._persona_natural_1.get_email(), "cor1@gmail.com")
        self.assertTrue(self._persona_natural_1.get_contrasena(), "contra1")

        self.assertEqual(self._admin.get_email(), "admin@admin.admin")
        self.assertTrue(self._admin.check_contrasena())

        self.assertEqual(self._actividad_tipo.get_nombre(), "estudiar")
        self.assertEqual(self._actividad_tipo.get_descripcion(), "estudiar mucho")
        self.assertEqual(self._actividad_tipo.get_categoria(), "academico")

        self.assertEqual(self._actividad_t.get_nombre(), "entrenar")
        self.assertEqual(self._actividad_t.get_descripcion(), "entrenar Voleibol")
        self.assertEqual(self._actividad_t.get_categoria(), "deportes")
        self.assertEqual(self._actividad_t.get_fecha_y_hora(), "2019/04/04 12:00:00")
        self.assertEqual(self._actividad_t.get_persona(), self._persona_natural_1)
        self.assertEqual(self._actividad_t.get_tiempo(), "real")

        self.assertEqual(self._actividad_p.get_nombre(), "jugar")
        self.assertEqual(self._actividad_p.get_descripcion(), "jugar Catan")
        self.assertEqual(self._actividad_p.get_categoria(), "ocio")
        self.assertEqual(self._actividad_p.get_fecha_y_hora(), "2019/04/05 13:30:00")
        self.assertEqual(self._actividad_p.get_persona(), self._persona_natural_2)
        self.assertEqual(self._actividad_p.get_tiempo(), "post")

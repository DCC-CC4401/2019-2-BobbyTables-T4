from django.test import TestCase
from BTT4App.models import *

class test_models(TestCase):

    def setUp(self):

        self._user1 = User.objects.create_user(first_name="nom1", last_name="ape1", email="cor1@gmail.com",
                                               username="cor1@gmail.com", password="contra1")
        self._persona_natural_1 = PersonaNatural(user=self._user1)

    def test_gets(self):

        self.assertTrue(self._persona_natural_1.user.check_password("contra1"))
        self.assertEqual(self._persona_natural_1.user.get_short_name(), "nom1")
        self.assertEqual(self._persona_natural_1.user.get_username(), "cor1@gmail.com")

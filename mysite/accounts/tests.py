from django.test import TestCase
from django.urls import reverse, reverse_lazy


class SignUpViewTests(TestCase):
    def test_true_is_true(self): #testing test
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_false_is_false(self): #testing test
        """ Tests if False is equal to False. Should always pass. """
        self.assertEqual(False, False)
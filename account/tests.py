from django.test import TestCase
from account.forms import RegistrationUserForm

class RegistrationUserFormTest(TestCase):

    def test_form_is_valid(self):
        form = RegistrationUserForm(data={'name': 'Иван', 'surname': 'Иванов', 'father_name': 'Иванович',
                                          'phone': '+375291234567', 'email': 'ivanov@mail.ru', 'password1': 'Ivanov123',
                                          'password2': 'Ivanov123'})
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form = RegistrationUserForm(data={'name': 'Иван', 'surname': 'Иванов', 'father_name': 'Иванович',
                                          'phone': '+375291234567', 'email': 'ivanov@mail', 'password1': 'Ivanov321',
                                          'password2': 'Ivanov123'})
        self.assertFalse(form.is_valid())

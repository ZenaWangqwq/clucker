
"""Unit tests of the sign up form."""
from django.test import TestCase
from django import forms
from microblogs.forms import LogInForm


class LogInFormTestCase(TestCase):
    """Unit tests of sign up form."""
    def setUp(self):
        self.form_input = {'username':'@janedoe','password':'Password123'}

    def test_forms_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username',form.fields)
        self.assertIn('password',form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))

    def test_form_acceptes_valid_input(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_blank_username(self):
        self.form_input['username'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_blank_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_accepts_incorrect_username(self):
        self.form_input['username'] = 'ja'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_accepts_incorrect_psw(self):
        self.form_input['password'] = 'psw'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_too_long_username(self):
        self.form_input['username'] = 'a' * 151  # Assuming the max length is 150
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_too_long_password(self):
        self.form_input['password'] = 'a' * 129  # Assuming the max length is 128
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

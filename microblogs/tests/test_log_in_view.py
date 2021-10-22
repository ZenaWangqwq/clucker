"""Tests of the log in view."""

from django.test import TestCase
from microblogs.forms import LogInForm
from django.urls import reverse
from microblogs.models import User
from .helpers import LogInTester

class SignUpViewTestCase(TestCase, LogInTester):
    """Tests of the log in view."""

    def setUp(self):
        self.url = reverse('log_in')
        User.objects.create_user('@janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            bio='Hello, I am Jane Doe.',
            password='Password123',
            )


    def test_log_in_url(self):
        self.assertEqual(self.url, '/log_in/')

    def test_get_log_in(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)

    def test_unsuccesful_log_in(self):
        form_input = {'username':'@janedoe','password':'WrongPassword123'}
        response = self.client.post(self.url,form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())

    def test_succesful_log_in(self):
        form_input = {'username':'@janedoe','password':'Password123'}
        response = self.client.post(self.url,form_input, follow=True)
        self.assertTrue(self._is_logged_in())
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code = 302, target_status_code = 200)
        self.assertTemplateUsed(response, 'feed.html')

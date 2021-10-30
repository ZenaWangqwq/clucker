"""Tests of the show user view."""

from django.test import TestCase
from django.urls import reverse
from microblogs.models import User



# class ShowUserCase(TestCase):
#     """Tests of the show_user view."""
#
#     def setUp(self):
#         self.url = reverse('show_user', kwargs={'user_id': id})
#
#     def test_show_user_url(self):
#         self.assertEqual(self.url, '/user/<int:user_id>/')
#
#     def test_get_show_user(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)

"""Tests of the user list view."""

from django.test import TestCase
from django.urls import reverse
from microblogs.models import User


class UserListViewTestCase(TestCase:
    """Tests of the log in view."""

    def setUp(self):
        self.url = reverse('user_list')
        self.users = User.objects.all()

    def test_user_list_url(self):
        self.assertEqual(self.url, '/users/')

    def test_get_user_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

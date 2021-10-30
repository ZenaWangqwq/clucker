"""Tests of the New Post view."""

from django.test import TestCase
from microblogs.forms import PostForm
from django.urls import reverse
from microblogs.models import User
from microblogs.models import Post


class NewPostTestCase(TestCase):
    """Tests of the new post view."""

    def setUp(self):
        self.url = reverse('new_post')
        first_name='Jane'
        last_name='Doe'
        username='@janedoe'
        email='janedoe@example.org'
        bio='My bio'

        user = User.objects.create_user(username)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.bio = bio

        post = Post.objects.create(
            author= user,
            text= "111111",
        )

    def test_new_post_url(self):
        self.assertEqual(self.url, '/new_post/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_post.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,PostForm))
        self.assertFalse(form.is_bound)

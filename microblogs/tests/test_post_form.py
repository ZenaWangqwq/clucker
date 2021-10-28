
"""Unit tests of the post form."""
from django.test import TestCase
from django import forms
from microblogs.forms import PostForm


class LPostFormTestCase(TestCase):
    """Unit tests of post form."""
    def setUp(self):
        self.form_input = {'text':'111111'}

    def test_valid_post_form(self):
        form = PostForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_forms_contains_required_fields(self):
        form = PostForm()
        self.assertIn('text',form.fields)

    def test_text_must_not_have_more_than_280_characters(self):
        self.form_input['text'] = 'x' * 281
        form = PostForm(data=self.form_input)
        self.assertFalse(form.is_valid())

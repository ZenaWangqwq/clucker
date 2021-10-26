"""Unit tests of the Post model."""
from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import Post
from microblogs.models import User

class PostTest(TestCase):
    """Unit tests of the Post model."""
    def setUp(self):
        self.user = User.objects.create_user(
            '@zena',
            first_name = 'Zena',
            last_name = 'Wang',
            email = "123456@qq.com",
            password = '1234password',
            bio = 'The quick brown fox jumps over the lazy dog.'
        )
        self.post = Post(author=self.user, text="xxxx")


    def test_valid_thing(self):
        self._assert_post_is_valid()

    def test_author_must_not_be_blank(self):
        self.post.author = None
        self._assert_post_is_invalid()

    def test_text_must_not_have_more_than_280_characters(self):
        self.post.text = 'x' * 281
        self._assert_post_is_invalid()

    # def test_created_at_is_set_just_once(self):
    #     self.post.created_at = 2021,1,1
    #     self._assert_post_is_invalid()

    def test_created_at_should_added_automatically(self):
        self.assertTrue(self.post.created_at != None)

    def _assert_post_is_valid(self, message="A valid thing was rejected"):
        try:
            self.post.full_clean()
        except ValidationError:
            self.fail(message)

    def _assert_post_is_invalid(self, message="An invalid thing was accepted"):
        try:
            self.post.full_clean()
            self.fail(message)
        except ValidationError:
            pass

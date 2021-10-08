from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

# Unit test goes here.
class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@zena',
            first_name = 'Zena',
            last_name = 'Wang',
            email = "123456@qq.com",
            password = '1234password',
            bio = 'The quick brown fox jumps over the lazy dog.'
        )

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_wrong()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_right()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_wrong()

    def test_user_should_be_unique(self):
        user = User.objects.create_user(
            '@zemei',
            first_name = 'Zemei',
            last_name = 'Wang',
            email = "111111@qq.com",
            password = '8888password',
            bio = 'This is Zemei profile.'
        )
        self.user.username = '@zemei'
        self._assert_wrong()

    def test_username_must_begin_with_at_symbol(self):
        self.user.username = '@zjam!ss'
        self._assert_wrong()

    def test_username_may_contain_number(self):
        self.user.username = '@zemei123'
        self._assert_right()

    def test_username_length_must_be_at_least_3 (self):
        self.user.username = '@as'
        self._assert_wrong()

    def test_username_must_be_contain_only_one_at (self):
        self.user.username = '@@zena'
        self._assert_wrong()

    def _assert_right(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail("Test user should be valid")

    def _assert_wrong(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

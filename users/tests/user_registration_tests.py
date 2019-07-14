from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import UserRegistrationForm
from users.views import register
import pytest


# @pytest.mark.skip(reason='need to concentrate on repirme app tests')
class TestUserRegistration(TestCase):
    """
    Tests if a new user can successfuly register and create a new account
    """

    def setUp(self):
        self.form = UserRegistrationForm({
            'username': 'testuser1',
            'email': 'test@mail.com',
            'password1': 'assert2019',
            'password2': 'assert2019'
        })

        self.form_invalid = UserRegistrationForm({
            'username': 'testuser1',
            'email': 'test@mail.com',
            'password1': '1233',
            'password2': '42536'
        })

    def test_register_page_loads_successfully(self):
        response = self.client.get(reverse(register))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse(register))
        self.assertTemplateUsed(response, 'users/register.html')

    def test_can_check_for_valid_data(self):
        assert self.form.is_valid()

    def test_can_save_valid_data(self):
        user = self.form.save()
        user_saved = User.objects.count()
        assert user_saved == 1
        assert user.username == 'testuser1'
        assert user.email == 'test@mail.com'

    def test_can_check_for_invalid_data(self):
        assert self.form_invalid.is_valid() is False

    def test_can_redirect_to_login(self):
        response = self.client.post(reverse(register), data={
            'username': 'testuser1',
            'email': 'test@mail.com',
            'password1': 'assert2019',
            'password2': 'assert2019'
        })

        self.assertRedirects(response,
                             reverse('login'),
                             status_code=302,
                             target_status_code=200)

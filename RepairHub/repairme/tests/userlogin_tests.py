from django.http import HttpResponse
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from repairme import views


class TestUserRegistration(TestCase):
    """
    Tests if a new user can successfuly register and create a new account
    """

    def test_register_page_loads_successfully(self):
        response = self.client.get(reverse(views.register))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse(views.register))
        self.assertTemplateUsed(response, 'register.html')

    def test_can_save_user_information(self):
        response = self.client.post(reverse(views.register), data={'username': 'testuser1',
                                                               'email': 'test@mail.com', 'password': 'assert2019'})
        assert response.status_code == 302
        assert User.objects.count() == 1

        test_user = User.objects.first()

        assert test_user.username == 'testuser1'
        assert test_user.email == 'test@mail.com'
        assert test_user.password == 'assert2019'


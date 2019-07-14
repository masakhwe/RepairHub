from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# @pytest.mark.skip(reason='need to concentrate on repirme app tests')
class TestUserLogin(TestCase):
    '''
        This class runs checks on user login
    '''

    def setUp(self):
        self.user = User.objects.create_user(username='logintester',
                                             email='login@mail.com',
                                             password='access2019')

    def test_login_page_loads_successfully(self):
        response = self.client.get(reverse('login'))
        assert response.status_code == 200

    def test_correct_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertTemplateNotUsed(response, 'users/register.html')

    def test_cannot_login_non_registered_user(self):
        response = self.client.login(username='testuser1',
                                     email='test@mail.com',
                                     password='assert2019')

        assert response is False

    def test_can_login_registered_user(self):
        response = self.client.login(username='logintester',
                                     password='access2019')
        assert response is True

    def test_can_redirect_to_home(self):
        response = self.client.post(reverse('login'), data={
                                    'username': 'logintester',
                                    'password': 'access2019'})

        self.assertRedirects(response,
                             reverse('repairme-home'),
                             status_code=302,
                             target_status_code=200)

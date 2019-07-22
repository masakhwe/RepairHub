from django.urls import reverse
from django.test import TestCase
from repairme.models import Repairs, Category
from django.contrib.auth.models import User


class TestRepairRequestRegistration(TestCase):
    """
    This class tests if a user can successfully make a repair request
    """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  email='test@mail.com',
                                                  password='tester247')

        self.client.login(username='testuser',
                          email='test@mail.com',
                          password='tester247')

        self.category = Category.objects.create(name='testcategory')

        self.data = {
            'device_name': 'sakara',
            'category': self.category.id,
            'serial_number': 'vssvsvwv52qa',
            'manufacturer': 'samsong',
            'description': 'detailed description',
        }

    def test_repair_request_page_loads_successfully(self):
        response = self.client.get(reverse('repairme-request'))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse('repairme-request'))
        self.assertTemplateUsed(response, 'repairme/repair_request.html')

    def test_repair_request_info_can_be_saved_to_db(self):
        self.client.post(reverse('repairme-request'), data=self.data)
        rep = Repairs.objects.all().first()

        assert Repairs.objects.count() == 1
        assert rep.owner == self.test_user
        assert rep.device_name == 'sakara'
        assert rep.serial_number == 'vssvsvwv52qa'
        assert rep.manufacturer == 'samsong'
        assert rep.description == 'detailed description'
        assert rep.photo == 'default.png'

    def test_can_redirect_to_homepage(self):
        response = self.client.post(reverse('repairme-request'),
                                    data=self.data)

        self.assertRedirects(response,
                             reverse('repairme-home'),
                             status_code=302,
                             target_status_code=200)

from django.test import TestCase
from repairme.models import Repairs, Category
from django.contrib.auth.models import User
from django.urls import reverse
# import pytest


class TestDetailedRepairRequest(TestCase):
    """
        This class tests if a user can view a single repair reguest in detail
    """

    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',
                                                  email='test@mail.com',
                                                  password='tester247')

        self.client.login(username='testuser',
                          email='test@mail.com',
                          password='tester247')

        self.category = Category.objects.create(name='testcategory')

        self.repair = Repairs.objects.create(device_name='sakara',
                                             category=self.category.id,
                                             serial_number='hghe4524awjkkk',
                                             manufacturer='manufact',
                                             description='how it happened')

    def test_detailed_repair_request_page_loads_successfully(self):
        response = self.client.get(reverse('repairme-detailed'))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse('repairme-detailed'))
        self.assertTemplateUsed(response, 'repairme/repair_detail.html')

    def test_can_retrieve_data_from_db(self):
        response = self.client.get(reverse('repairme-detailed'), {'pk': 1})

        assert response.data.owner == self.test_user
        assert response.data.device_name == 'sakara'
        assert response.category == self.category.id
        assert response.data.serial_number == 'hghe4524awjkkk'
        assert response.data.manufacturer == 'manufact'
        assert response.data.description == 'how it happened'

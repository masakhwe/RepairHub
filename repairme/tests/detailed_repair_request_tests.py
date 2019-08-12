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

        self.repair = Repairs.objects.create(owner=self.test_user,
                                             device_name='sakara',
                                             category=self.category,
                                             serial_number='hghe4524awjkkk',
                                             manufacturer='manufact',
                                             description='how it happened')

    def test_repairs_list_page_loads_successfully(self):
        response = self.client.get(reverse('repairs_list'))
        assert response.status_code == 200

    def test_detailed_repair_request_page_loads_successfully(self):
        response = self.client.get(reverse('repair-detail', kwargs={'pk': self.repair.id}))
        assert response.status_code == 200

    def test_correct_template_for_repairs_list(self):
        response = self.client.get(reverse('repairs_list'))
        self.assertTemplateUsed(response, 'repairme/repair_request_list.html')

    def test_correct_template_for_detailed_repair_request(self):
        response = self.client.get(reverse('repair-detail', kwargs={'pk': self.repair.id}))
        self.assertTemplateUsed(response, 'repairme/repair_detail.html')

    def test_can_retrieve_data_from_db(self):
        response = self.client.get(reverse('repair-detail', kwargs={'pk': self.repair.id}))
        assert response.status_code == 200

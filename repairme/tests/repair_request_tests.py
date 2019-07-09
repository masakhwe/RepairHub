from django.urls import reverse
from django.test import TestCase
from repairme.models import Repairs
from repairme.forms import RepairRequestForm
from repairme.views import repair_request


class TestRepairRequestRegistration(TestCase):
    """
    This class tests if a user can successfully make a repair request
    """

    def setUp(self):
        self.repair_form = RepairRequestForm({
            'customer_name': 'testcustomer1',
            'repair_category': 'entertainment',
        })

    def test_repair_request_page_loads_successfully(self):
        response = self.client.get(reverse(repair_request))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse(repair_request))
        self.assertTemplateUsed(response, 'repairme/repair_request.html')

    def test_repair_request_info_can_be_saved_to_db(self):
        repair = self.repair_form.save()
        repair_request_saved = Repairs.objects.count()

        assert repair_request_saved == 1
        assert repair.customer_name == 'testcustomer1'

    def test_can_redirect_to_homepage(self):
        response = self.client.post(reverse(repair_request), data={
            'customer_name': 'testcustomer1',
        })

        self.assertRedirects(response,
                             reverse('home'),
                             status_code=302,
                             target_status_code=200)

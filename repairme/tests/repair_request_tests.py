from django.urls import reverse
from django.test import TestCase
from repairme.models import Repairs, Category
from django.contrib.auth.models import User
from repairme.forms import RepairRequestForm
from repairme.views import repair_request
# from django.core.files.uploadedfile import SimpleUploadedFile


class TestRepairRequestRegistration(TestCase):
    """
    This class tests if a user can successfully make a repair request
    """

    def setUp(self):
        self.owner = User.objects.create(username='testuser',
                                         email='test@mail.com',
                                         password='tester247')

        self.category = Category.objects.create(name='testcategory')

        data = {
            'owner': self.owner.id,
            'device_name': 'sakara',
            'category': self.category.id,
            'serial_number': 'vssvsvwv52qa',
            'manufacturer': 'samsong',
            'description': 'detailed description',
        }
        '''
        file_data = {'photo': SimpleUploadedFile('test_image.jpeg',
                                                 open('media/', 'rb'),
                                                 content_type='image/jpeg')}
        '''
        self.form = RepairRequestForm(data)

    def test_repair_request_page_loads_successfully(self):
        response = self.client.get(reverse(repair_request))
        assert response.status_code == 200

    def test_right_template_used(self):
        response = self.client.get(reverse(repair_request))
        self.assertTemplateUsed(response, 'repairme/repair_request.html')

    def test_form_is_valid(self):
        assert self.form.is_valid() is True

        form_saved = self.form.save()
        assert form_saved.device_name == 'sakara'
        assert form_saved.serial_number == 'vssvsvwv52qa'
        assert form_saved.manufacturer == 'samsong'
        assert form_saved.description == 'detailed description'
        assert form_saved.photo == 'default.png'

    # @pytest.mark.skip()
    def test_repair_request_info_can_be_saved_to_db(self):
        self.form.save()
        rep = Repairs.objects.all().first()

        assert Repairs.objects.count() == 1
        assert rep.device_name == 'sakara'
        assert rep.serial_number == 'vssvsvwv52qa'
        assert rep.manufacturer == 'samsong'
        assert rep.description == 'detailed description'
        assert rep.photo == 'default.png'

    # @pytest.mark.skip()
    def test_can_redirect_to_homepage(self):
        response = self.client.post(reverse(repair_request), data={
            'owner': self.owner.id,
            'device_name': 'sakara',
            'category': self.category.id,
            'serial_number': 'vssvsvwv52qa',
            'manufacturer': 'samsong',
            'description': 'detailed description',
        })

        self.assertRedirects(response,
                             reverse('repairme-home'),
                             status_code=302,
                             target_status_code=200)

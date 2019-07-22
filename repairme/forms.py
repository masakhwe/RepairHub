from django.forms import ModelForm
from repairme.models import Repairs


class RepairRequestForm(ModelForm):

    class Meta:
        model = Repairs

        fields = [
            'device_name',
            'category',
            'serial_number',
            'manufacturer',
            'description',
            'photo'
        ]

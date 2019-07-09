from django import forms
from .models import Repairs


class RepairRequestForm(forms.Form):

    class Meta:
        model = Repairs

        fields = [
            'Customer Name',
            'Item Name',
            'Serial Number',
            'Manufacturer',
            'Photo',
            'Fault Date',
        ]

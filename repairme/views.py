from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from repairme.models import Repairs
from repairme.forms import RepairRequestForm
from django.contrib.messages.views import SuccessMessageMixin


class RepairRequestView(SuccessMessageMixin, CreateView):
    model = Repairs
    form_class = RepairRequestForm
    template_name = 'repairme/repair_request.html'
    success_url = '/'
    success_message = 'Your Repair Request was Successfully Saved'


class HomeView(TemplateView):
    template_name = 'repairme/home.html'

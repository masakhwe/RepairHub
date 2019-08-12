from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from repairme.models import Repairs
from repairme.forms import RepairRequestForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


class RepairRequestView(SuccessMessageMixin, CreateView):
    model = Repairs
    form_class = RepairRequestForm
    template_name = 'repairme/repair_request.html'
    success_url = '/'
    success_message = 'Your Repair Request was Successfully Saved'

    def form_valid(self, form_class):
        '''To assign owner attribute the authenicated user'''
        form_class.instance.owner = self.request.user
        return super().form_valid(form_class)


class HomeView(TemplateView):
    template_name = 'repairme/home.html'


class RepairsListView(ListView):
    model = Repairs
    context_object_name = 'repairs_request_list'
    template_name = 'repairme/repair_request_list.html'


class RepairDetail(DetailView):
    model = Repairs
    context_object_name = 'repair_detail'
    template_name = 'repairme/repair_detail.html'

from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserRegistrationForm  # custom registration form


class Register(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = 'login'
    success_message = 'Account Successfully created'


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

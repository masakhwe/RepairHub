from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from repairme.forms import RepairRequestForm
from django.contrib import messages


def home(request):
    return render(request, 'repairme/home.html')


def repair_request(request):
    if request.method == "POST":
        form = RepairRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,
                             "Your Repair Request was Successfully saved")
            return redirect('repairme-home')
    else:
        form = RepairRequestForm()

    return render(request, 'repairme/repair_request.html', {'form': form})

from django.shortcuts import render


def home(request):
    return render(request, 'repairme/home.html')


def repair_request(request):
    return render(request, 'repairme/repair_request.html')

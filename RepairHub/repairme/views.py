from django.shortcuts import render


def home(request):
    return render(request, "repairme/home.html")


def about(request):
    return render(request, "repairme/about.html")

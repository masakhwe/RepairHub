from django.urls import path
from .views import home, repair_request

urlpatterns = [
    path('', home, name='repairme-home'),
    path('repair_request', repair_request, name='repairme-request'),
]

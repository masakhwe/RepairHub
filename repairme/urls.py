from django.urls import path
from .views import HomeView, RepairRequestView

urlpatterns = [
    path('', HomeView.as_view(), name='repairme-home'),

    path('repair_request', RepairRequestView.as_view(),
         name='repairme-request'),
]

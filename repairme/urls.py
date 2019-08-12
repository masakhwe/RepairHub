from django.urls import path
from .views import HomeView, RepairRequestView, RepairsListView, RepairDetail

urlpatterns = [
    path('', HomeView.as_view(), name='repairme-home'),

    path('repair_request', RepairRequestView.as_view(),
         name='repairme-request'),

    path('repairs', RepairsListView.as_view(), name='repairs_list'),

    path('repairs/<int:pk>', RepairDetail.as_view(),
         name='repair-detail'),
]

from django.urls import path

from api.views import DeviceListView, DeviceDetailView, DeviceResultsView


urlpatterns = [
    path('', DeviceListView.as_view(), name='device-list'),
    path('<str:slug>/', DeviceDetailView.as_view(), name='device-detail'),
]
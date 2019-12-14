from django.urls import path

from api.views import DeviceList, DeviceDetail


urlpatterns = [
    path('', DeviceList.as_view(), name='device-list'),
    path('<str:slug>/', DeviceDetail.as_view(), name='device-detail'),
]
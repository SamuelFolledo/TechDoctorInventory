from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from inventories.models import Device
from api.serializers import DeviceSerializer

class DeviceList(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(RetrieveDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
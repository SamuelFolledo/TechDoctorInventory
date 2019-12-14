from rest_framework.serializers import ModelSerializer

from inventories.models import Device

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
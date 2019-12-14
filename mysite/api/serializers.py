from rest_framework.serializers import ModelSerializer

from wiki.models import Device

class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
from rest_framework import serializers
from .models import GHGEnergyMeter

class GHGEnergyMeterSerializer(serializers.Serializer):
  meter = serializers.IntegerField()
  interval = serializers.IntegerField()
  Kt = serializers.FloatField()
  
  def create(self, validated_data):
    return GHGEnergyMeter.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.meter = validated_data.get('meter', instance.meter)
    instance.interval = validated_data.get('interval', instance.interval)
    instance.Kt = validated_data.get('Kt', instance.Kt)
    instance.save()
    return instance

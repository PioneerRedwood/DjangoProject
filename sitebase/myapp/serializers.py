from rest_framework import serializers
from .models import Population


class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = ('id', 'do', 'sigu', 'dong', 'population')

    def create(self, validated_data):
        return Population.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.do = validated_data.get('do', instance.do)
        instance.sigu = validated_data('sigu', instance.sigu)
        instance.dong = validated_data('dong', instance.dong)
        instance.population = validated_data('population', instance.population)
        instance.save()
        return instance

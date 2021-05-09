from rest_framework import serializers
from .models import Population
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PopulationSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Population
        fields = ('id', 'do', 'sigu', 'dong', 'population')
        read_only_fields = ('population',)

    def create(self, validated_data):
        return Population.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.do = validated_data.get('do', instance.do)
        instance.sigu = validated_data('sigu', instance.sigu)
        instance.dong = validated_data('dong', instance.dong)
        instance.population = validated_data('population', instance.population)
        instance.save()
        return instance

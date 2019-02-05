from . import models

from rest_framework import serializers


class lawOfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.lawOffice
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'address', 
            'phone', 
            'email', 
        )


class LawyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lawyer
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Administrator
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )



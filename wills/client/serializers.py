from . import models

from rest_framework import serializers


class ClientSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClientSession
        fields = (
            'pk', 
            'created', 
            'last_updated', 
        )


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'occupation', 
            'address', 
            'home_telephone', 
            'work_telephone', 
            'domicile', 
            'dob', 
            'place_of_birth', 
            'name_at_birth', 
            'marital_status', 
        )


class SpouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Spouse
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'domicile', 
            'dob', 
            'place_of_birth', 
            'dom', 
            'place_of_marriage', 
            'marriage_contract_exists', 
            'marriage_contract', 
            'seperated', 
            'divorced', 
            'dos', 
            'dod', 
            'divorce_contract', 
        )


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Child
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'dob', 
            'live_in', 
            'address', 
            'notes', 
            'custody', 
            'adopted', 
            'legitimate', 
        )



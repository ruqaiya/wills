from . import models
from . import serializers
from rest_framework import viewsets, permissions


class ClientSessionViewSet(viewsets.ModelViewSet):
    """ViewSet for the ClientSession class"""

    queryset = models.ClientSession.objects.all()
    serializer_class = serializers.ClientSessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpouseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Spouse class"""

    queryset = models.Spouse.objects.all()
    serializer_class = serializers.SpouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChildViewSet(viewsets.ModelViewSet):
    """ViewSet for the Child class"""

    queryset = models.Child.objects.all()
    serializer_class = serializers.ChildSerializer
    permission_classes = [permissions.IsAuthenticated]



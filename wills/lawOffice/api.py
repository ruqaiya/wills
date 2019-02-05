from . import models
from . import serializers
from rest_framework import viewsets, permissions


class lawOfficeViewSet(viewsets.ModelViewSet):
    """ViewSet for the lawOffice class"""

    queryset = models.lawOffice.objects.all()
    serializer_class = serializers.lawOfficeSerializer
    permission_classes = [permissions.IsAuthenticated]


class LawyerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Lawyer class"""

    queryset = models.Lawyer.objects.all()
    serializer_class = serializers.LawyerSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdministratorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Administrator class"""

    queryset = models.Administrator.objects.all()
    serializer_class = serializers.AdministratorSerializer
    permission_classes = [permissions.IsAuthenticated]



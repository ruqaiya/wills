from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class lawOffice(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('lawOffice_lawoffice_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('lawOffice_lawoffice_update', args=(self.slug,))


class Lawyer(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="LawyerProfile"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('lawOffice_lawyer_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('lawOffice_lawyer_update', args=(self.slug,))


class Administrator(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="AdministratorProfile"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('lawOffice_administrator_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('lawOffice_administrator_update', args=(self.slug,))

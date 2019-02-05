from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import FileField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class ClientSession(models.Model):

    # Fields
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    client = models.OneToOneField(
        'client.Client',
        on_delete=models.CASCADE, related_name="client"
    )

    lawyer = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE, related_name="lawyer"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return u'%s' % self.client.name

    def get_absolute_url(self):
        return reverse('client_clientsession_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('client_clientsession_update', args=(self.pk,))


class Client(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    occupation = CharField(max_length=100)
    address = CharField(max_length=500)
    home_telephone = CharField(max_length=30)
    work_telephone = CharField(max_length=100, null=True, blank=True)
    domicile = CharField(max_length=100)
    dob = DateField()
    place_of_birth = CharField(max_length=100)
    name_at_birth = CharField(max_length=255)
    marital_status = CharField(max_length=100)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="ClientLoginProfile", null=True
    )


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('client_client_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('client_client_update', args=(self.slug,))


class Spouse(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    domicile = CharField(max_length=100)
    dob = DateField()
    place_of_birth = CharField(max_length=100)
    dom = DateField()
    place_of_marriage = CharField(max_length=100)
    marriage_contract_exists = BooleanField()
    marriage_contract = FileField(upload_to="media/", null=True, blank=True)
    seperated = BooleanField()
    divorced = BooleanField()
    dos = DateField(null=True, blank=True)
    dod = DateField(null=True, blank=True)
    divorce_contract = FileField(upload_to="media/", null=True, blank=True)

    # Relationship Fields
    session = models.ForeignKey(
        'client.ClientSession',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.name

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('client_spouse_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('client_spouse_update', args=(self.slug,))


class Child(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    dob = DateField()
    live_in = BooleanField()
    address = CharField(max_length=200, null=True, blank=True)
    notes = TextField(max_length=5000, null=True, blank=True)
    custody = BooleanField()
    adopted = BooleanField()
    legitimate = BooleanField()

    # Relationship Fields
    session = models.ForeignKey(
        'client.ClientSession',
        on_delete=models.CASCADE, related_name="clientsession"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('client_child_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('client_child_update', args=(self.slug,))

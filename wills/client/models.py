from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import FileField
from django.db.models import TextField
from django.conf import settings
from django.db import models as models


class ClientSession(models.Model):

    # Fields
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    assign_executor = BooleanField(default=False)

    # Relationship Fields
    client = models.OneToOneField(
        'client.Client',
        on_delete=models.CASCADE, related_name="client"
    )

    lawyer = models.ForeignKey(
        'lawOffice.Lawyer',
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

    # Choices Values
    MARRIED = 'MR'
    SINGLE = 'SL'
    LIVINGTOGETHER = 'LT'
    MARRIED_STATUS_CHOICES = (
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (LIVINGTOGETHER, 'Living together')
    )

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    occupation = CharField(max_length=100, null=True, blank=True)
    address = CharField(max_length=500)
    home_telephone = CharField(max_length=30, null=True, blank=True)
    work_telephone = CharField(max_length=100, null=True, blank=True)
    domicile = CharField(max_length=100, null=True, blank=True)
    dob = DateField(null=True, blank=True)
    place_of_birth = CharField(max_length=100, null=True, blank=True)
    name_at_birth = CharField(max_length=255, null=True, blank=True)
    marital_status = CharField(max_length=2, choices=MARRIED_STATUS_CHOICES, default=SINGLE)

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
    dob = DateField(null=True, blank=True)
    place_of_birth = CharField(max_length=100, null=True, blank=True)
    dom = DateField(null=True, blank=True)
    place_of_marriage = CharField(max_length=100, null=True, blank=True)
    marriage_contract_exists = BooleanField(default=False)
    marriage_contract = FileField(upload_to="media/", null=True, blank=True)
    seperated = BooleanField(default=False)
    divorced = BooleanField(default=False)
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
    live_in = BooleanField(default=True)
    address = CharField(max_length=200, null=True, blank=True)
    notes = TextField(max_length=5000, null=True, blank=True)
    custody = BooleanField(default=False)
    adopted = BooleanField(default=False)
    legitimate = BooleanField(default=True)

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


class Executor(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    address = CharField(max_length=200, null=True, blank=True)
    notes = TextField(max_length=5000, null=True, blank=True)

    session = models.ForeignKey(
        'client.ClientSession',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('client_executor_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('client_executor_update', args=(self.slug,))


class ChildCareTaker(models.Model):

    # Fields
    name = CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    address = CharField(max_length=200, null=True, blank=True)
    notes = TextField(max_length=5000, null=True, blank=True)

    session = models.ForeignKey(
        'client.ClientSession',
        on_delete=models.CASCADE
    )

    child = models.ForeignKey(
        'client.Child',
        on_delete=models.CASCADE, related_name="CareTaker"
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def __str__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('client_caretaker_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('client_caretaker_update', args=(self.slug,))

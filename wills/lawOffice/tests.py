import unittest
from django.urls import reverse
from django.test import Client
from .models import lawOffice, Lawyer, Administrator
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_lawoffice(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["address"] = "address"
    defaults["phone"] = "phone"
    defaults["email"] = "email"
    defaults.update(**kwargs)
    return lawOffice.objects.create(**defaults)


def create_lawyer(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Lawyer.objects.create(**defaults)


def create_administrator(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Administrator.objects.create(**defaults)


class lawOfficeViewTest(unittest.TestCase):
    '''
    Tests for lawOffice
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lawoffice(self):
        url = reverse('lawOffice_lawoffice_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lawoffice(self):
        url = reverse('lawOffice_lawoffice_create')
        data = {
            "name": "name",
            "address": "address",
            "phone": "phone",
            "email": "email",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lawoffice(self):
        lawoffice = create_lawoffice()
        url = reverse('lawOffice_lawoffice_detail', args=[lawoffice.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lawoffice(self):
        lawoffice = create_lawoffice()
        data = {
            "name": "name",
            "address": "address",
            "phone": "phone",
            "email": "email",
        }
        url = reverse('lawOffice_lawoffice_update', args=[lawoffice.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LawyerViewTest(unittest.TestCase):
    '''
    Tests for Lawyer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_lawyer(self):
        url = reverse('lawOffice_lawyer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_lawyer(self):
        url = reverse('lawOffice_lawyer_create')
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_lawyer(self):
        lawyer = create_lawyer()
        url = reverse('lawOffice_lawyer_detail', args=[lawyer.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_lawyer(self):
        lawyer = create_lawyer()
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('lawOffice_lawyer_update', args=[lawyer.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AdministratorViewTest(unittest.TestCase):
    '''
    Tests for Administrator
    '''
    def setUp(self):
        self.client = Client()

    def test_list_administrator(self):
        url = reverse('lawOffice_administrator_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_administrator(self):
        url = reverse('lawOffice_administrator_create')
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_administrator(self):
        administrator = create_administrator()
        url = reverse('lawOffice_administrator_detail', args=[administrator.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_administrator(self):
        administrator = create_administrator()
        data = {
            "name": "name",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('lawOffice_administrator_update', args=[administrator.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



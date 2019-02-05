import unittest
from django.urls import reverse
from django.test import Client
from .models import ClientSession, Client, Spouse, Child
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


def create_clientsession(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "client" not in defaults:
        defaults["client"] = create_client()
    return ClientSession.objects.create(**defaults)


def create_client(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["occupation"] = "occupation"
    defaults["address"] = "address"
    defaults["home_telephone"] = "home_telephone"
    defaults["work_telephone"] = "work_telephone"
    defaults["domicile"] = "domicile"
    defaults["dob"] = "dob"
    defaults["place_of_birth"] = "place_of_birth"
    defaults["name_at_birth"] = "name_at_birth"
    defaults["marital_status"] = "marital_status"
    defaults.update(**kwargs)
    return Client.objects.create(**defaults)


def create_spouse(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["domicile"] = "domicile"
    defaults["dob"] = "dob"
    defaults["place_of_birth"] = "place_of_birth"
    defaults["dom"] = "dom"
    defaults["place_of_marriage"] = "place_of_marriage"
    defaults["marriage_contract_exists"] = "marriage_contract_exists"
    defaults["marriage_contract"] = "marriage_contract"
    defaults["seperated"] = "seperated"
    defaults["divorced"] = "divorced"
    defaults["dos"] = "dos"
    defaults["dod"] = "dod"
    defaults["divorce_contract"] = "divorce_contract"
    defaults.update(**kwargs)
    if "session" not in defaults:
        defaults["session"] = create_clientsession()
    return Spouse.objects.create(**defaults)


def create_child(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults["dob"] = "dob"
    defaults["live_in"] = "live_in"
    defaults["address"] = "address"
    defaults["notes"] = "notes"
    defaults["custody"] = "custody"
    defaults["adopted"] = "adopted"
    defaults["legitimate"] = "legitimate"
    defaults.update(**kwargs)
    if "session" not in defaults:
        defaults["session"] = create_clientsession()
    return Child.objects.create(**defaults)


class ClientSessionViewTest(unittest.TestCase):
    '''
    Tests for ClientSession
    '''
    def setUp(self):
        self.client = Client()

    def test_list_clientsession(self):
        url = reverse('client_clientsession_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_clientsession(self):
        url = reverse('client_clientsession_create')
        data = {
            "client": create_client().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_clientsession(self):
        clientsession = create_clientsession()
        url = reverse('client_clientsession_detail', args=[clientsession.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_clientsession(self):
        clientsession = create_clientsession()
        data = {
            "client": create_client().pk,
        }
        url = reverse('client_clientsession_update', args=[clientsession.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ClientViewTest(unittest.TestCase):
    '''
    Tests for Client
    '''
    def setUp(self):
        self.client = Client()

    def test_list_client(self):
        url = reverse('client_client_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_client(self):
        url = reverse('client_client_create')
        data = {
            "name": "name",
            "slug": "slug",
            "occupation": "occupation",
            "address": "address",
            "home_telephone": "home_telephone",
            "work_telephone": "work_telephone",
            "domicile": "domicile",
            "dob": "dob",
            "place_of_birth": "place_of_birth",
            "name_at_birth": "name_at_birth",
            "marital_status": "marital_status",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_client(self):
        client = create_client()
        url = reverse('client_client_detail', args=[client.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_client(self):
        client = create_client()
        data = {
            "name": "name",
            "slug": "slug",
            "occupation": "occupation",
            "address": "address",
            "home_telephone": "home_telephone",
            "work_telephone": "work_telephone",
            "domicile": "domicile",
            "dob": "dob",
            "place_of_birth": "place_of_birth",
            "name_at_birth": "name_at_birth",
            "marital_status": "marital_status",
        }
        url = reverse('client_client_update', args=[client.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SpouseViewTest(unittest.TestCase):
    '''
    Tests for Spouse
    '''
    def setUp(self):
        self.client = Client()

    def test_list_spouse(self):
        url = reverse('client_spouse_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_spouse(self):
        url = reverse('client_spouse_create')
        data = {
            "name": "name",
            "slug": "slug",
            "domicile": "domicile",
            "dob": "dob",
            "place_of_birth": "place_of_birth",
            "dom": "dom",
            "place_of_marriage": "place_of_marriage",
            "marriage_contract_exists": "marriage_contract_exists",
            "marriage_contract": "marriage_contract",
            "seperated": "seperated",
            "divorced": "divorced",
            "dos": "dos",
            "dod": "dod",
            "divorce_contract": "divorce_contract",
            "session": create_clientsession().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_spouse(self):
        spouse = create_spouse()
        url = reverse('client_spouse_detail', args=[spouse.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_spouse(self):
        spouse = create_spouse()
        data = {
            "name": "name",
            "slug": "slug",
            "domicile": "domicile",
            "dob": "dob",
            "place_of_birth": "place_of_birth",
            "dom": "dom",
            "place_of_marriage": "place_of_marriage",
            "marriage_contract_exists": "marriage_contract_exists",
            "marriage_contract": "marriage_contract",
            "seperated": "seperated",
            "divorced": "divorced",
            "dos": "dos",
            "dod": "dod",
            "divorce_contract": "divorce_contract",
            "session": create_clientsession().pk,
        }
        url = reverse('client_spouse_update', args=[spouse.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ChildViewTest(unittest.TestCase):
    '''
    Tests for Child
    '''
    def setUp(self):
        self.client = Client()

    def test_list_child(self):
        url = reverse('client_child_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_child(self):
        url = reverse('client_child_create')
        data = {
            "name": "name",
            "slug": "slug",
            "dob": "dob",
            "live_in": "live_in",
            "address": "address",
            "notes": "notes",
            "custody": "custody",
            "adopted": "adopted",
            "legitimate": "legitimate",
            "session": create_clientsession().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_child(self):
        child = create_child()
        url = reverse('client_child_detail', args=[child.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_child(self):
        child = create_child()
        data = {
            "name": "name",
            "slug": "slug",
            "dob": "dob",
            "live_in": "live_in",
            "address": "address",
            "notes": "notes",
            "custody": "custody",
            "adopted": "adopted",
            "legitimate": "legitimate",
            "session": create_clientsession().pk,
        }
        url = reverse('client_child_update', args=[child.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



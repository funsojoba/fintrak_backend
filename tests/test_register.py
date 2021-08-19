from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class TestCreateUser(APITestCase):
    def setUp(self):
        self.url = reverse('register')
        self.valid_payload = {
            "first_name":"John",
            "last_name":"Doe",
            "email":"john@doe.com",
            "password":"johndoe12345"
        }
        self.invalid_payload = {
            "first_name":"",
            "last_name":"",
            "email":"",
            "password":""
        }
    
    def test_user_can_register_with_valid_payload(self):
        res = self.client.post(self.url, self.valid_payload)
        self.assertEqual(res.status_code, 201)
    
    def test_user_cannot_register_with_invalid_payload(self):
        res = self.client.post(self.url, self.invalid_payload)
        self.assertEqual(res.status_code, 400)
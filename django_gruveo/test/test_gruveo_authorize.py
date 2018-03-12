import requests
from django.conf import settings
from django.test import TestCase, Client
from faker import Faker

from django.test.client import RequestFactory


class ActivationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()
        self.factory = RequestFactory()
        settings.GRUVEO_SECRET = 'W62wB9JjW3tFyUMtF5QhRSbk' #gruveo demo secret

    def test_validate_valid_token(self):
        token = self.fake.pystr(min_chars=1, max_chars=20)
        data = {
            'token': token
        }
        response = self.client.post('/gruveo/token/', data)

        headers = {'Content-type': 'text/plain'}
        r = requests.post('https://api-demo.gruveo.com/signer', data=token, headers=headers)

        self.assertEquals(response.status_code, 201)
        self.assertEquals(r.status_code, 200)
        self.assertEquals(response.json()['token_hmac'], r.text)

    def test_validate_null_token(self):
        token = ""
        data = {
            'token': token
        }
        response = self.client.post('/gruveo/token/', data)

        self.assertEquals(response.status_code, 400)

    def test_validate_invalid_body(self):
        token = ""
        data = {
            'tokens': token
        }
        response = self.client.post('/gruveo/token/', data)

        self.assertEquals(response.status_code, 400)

    def test_validate_invalid_key_secret(self):
        settings.GRUVEO_SECRET =  self.fake.pystr(min_chars=1, max_chars=20)
        token = self.fake.pystr(min_chars=1, max_chars=20)
        data = {
            'tokens': token
        }
        response = self.client.post('/gruveo/token/', data)

        self.assertEquals(response.status_code, 400)
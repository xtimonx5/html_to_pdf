import os
import json

from django.test import override_settings
from django.conf import settings
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from unittest import TestCase


class PDFApiGenerator(TestCase):
    def setUp(self):
        self.client = APIClient()

    @staticmethod
    def get_path(file_path):
        file_name = file_path.split('/')[-1]
        return os.path.join(settings.REPORT_ROOT, file_name)

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_generate_from_link(self):
        response = self.client.post('/gen_pdf/link_to_pdf/',
                                    data={'html': 'http://google.com/'})  # i hope, google still will be available :)
        response_dict = json.loads(response.content)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIn('url', response_dict.keys())
        self.assertTrue(os.path.isfile(self.get_path(response_dict['url'])))  # asserts that file exists

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_generate_from_link_invalid_params(self):
        response = self.client.post('/gen_pdf/link_to_pdf/',
                                    data={'html': 'SomeInvalidLink'})
        json.loads(response.content)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_generate_from_file(self):
        with open('tests/files/index.html') as fp:
            response = self.client.post('/gen_pdf/file_to_pdf/',
                                        data={'html': fp}, format='multipart')
            response_dict = json.loads(response.content)
            self.assertEqual(response.status_code, HTTP_200_OK)
            self.assertIn('url', response_dict.keys())
            self.assertTrue(os.path.isfile(self.get_path(response_dict['url'])))  # asserts that file exists

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_generate_from_file_invalid_params(self):
        with open('tests/files/index.nothtml') as fp:
            response = self.client.post('/gen_pdf/file_to_pdf/',
                                        data={'html': fp}, format='multipart')
            json.loads(response.content)
            self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

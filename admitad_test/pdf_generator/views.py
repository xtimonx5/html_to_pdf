import os
from urllib.parse import urljoin

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from pdf_generator.generator_classes import HtmlToPDFGenerator
from pdf_generator.serializers import (
    LinkToHtmlSerializer,
    FileToHtmlSerializer,
)


class GeneratePdfApiViewSet(GenericViewSet):
    serializer_class = LinkToHtmlSerializer

    def get_generator_class(self):
        """
        To be changed in case, if we'll need to generate files with other extensions based on query arg (http://url?extension=png, xls and so on)
        :return: generator realized by GenericHtmlGenerator. 
        """
        return HtmlToPDFGenerator

    @staticmethod
    def get_url_for_file(report_name):
        return urljoin(settings.REPORT_URL, report_name)

    def save_file_to_storage(self):
        file_obj = self.request.data['html']
        file_path = default_storage.save(file_obj.name, ContentFile(file_obj.read()))
        return os.path.join(settings.MEDIA_ROOT, file_path)

    def validate_payload(self, payload):
        self.serializer_class(data=payload).is_valid(raise_exception=True)

    @action(methods=['POST', ], detail=False, serializer_class=FileToHtmlSerializer)
    def file_to_pdf(self, request, *args, **kwargs):
        self.validate_payload(self.request.data)

        filepath = self.save_file_to_storage()
        payload = {'html': filepath}
        generator_class = self.get_generator_class()
        generator = generator_class(payload)
        generator.generate_file()

        return Response(status=200, data={'url': self.get_url_for_file(generator.report_name)})

    @action(methods=['POST', ], detail=False, serializer_class=LinkToHtmlSerializer)
    def link_to_pdf(self, request, *args, **kwargs):
        self.validate_payload(self.request.data)
        generator_class = self.get_generator_class()
        generator = generator_class(payload=request.data)
        generator.generate_file()
        return Response(status=200, data={'url': self.get_url_for_file(generator.report_name)})

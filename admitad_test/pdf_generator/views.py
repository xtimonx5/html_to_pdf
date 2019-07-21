from django.views.generic import TemplateView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from pdf_generator.generator_classes import PdfToHtmlGenerator
import uuid
from pdf_generator.serializers import (
    LinkToHtmlSerializer,
    FileToHtmlSerializer,
)


class IndexView(TemplateView):
    template_name = 'index.html'


class GeneratePdfApiView(GenericViewSet):
    def get_serializer_class(self):
        link = self.request.data.get('html')
        if link:
            return LinkToHtmlSerializer

        # todo: add file serializer
        return FileToHtmlSerializer

    def get_html_item(self):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def get_generator_class(self):
        """
        To be changed in case, if we'll need to generate files with other extensions. (png, xls and so on)
        :return: generator realized by GenericHtmlGenerator. 
        """
        return PdfToHtmlGenerator

    def post(self, request, *args, **kwargs):
        html_item = self.get_html_item()
        report_name = f'{uuid.uuid4()}.pdf'
        generator_class = self.get_generator_class()
        generator_class(html_item).generate_file(report_name)

        return Response(status=200, data={'a': report_name})

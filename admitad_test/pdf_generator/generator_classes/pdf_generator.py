import os

from django.conf import settings

from .generic_generator import GenericHtmlGenerator


class PdfToHtmlGenerator(GenericHtmlGenerator):
    def generate_file(self, report_name=None) -> None:
        self.html_to_generate.write_pdf(os.path.join(settings.REPORT_ROOT, report_name))

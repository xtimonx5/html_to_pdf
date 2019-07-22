import uuid
from weasyprint import HTML

from pdf_generator.tasks import generate_file
from .generic_generator import GenericHtmlGenerator


class HtmlToPDFGenerator(GenericHtmlGenerator):
    def get_report_name(self):
        return f'{uuid.uuid4()}.pdf'

    def generate_file(self, report_name=None, async_generation=True) -> None:
        kwargs = {
            'source': self.source,
            'report_name': report_name or self.report_name
        }
        if async_generation:
            generate_file.apply_async(kwargs=kwargs)
        else:
            generate_file(**kwargs)

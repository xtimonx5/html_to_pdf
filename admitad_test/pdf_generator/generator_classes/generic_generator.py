from abc import ABC

from weasyprint import HTML


class GenericHtmlGenerator(ABC):
    def __init__(self, html_to_generate: HTML):
        self.html_to_generate = html_to_generate

    def generate_file(self, report_name=None) -> None:
        raise NotImplementedError

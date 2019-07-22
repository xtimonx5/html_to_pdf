from abc import ABC

from weasyprint import HTML


class GenericHtmlGenerator(ABC):
    report_name = None

    def __init__(self, payload):
        self.source = payload.get('html')
        self.report_name = self.report_name if self.report_name else self.get_report_name()

    def get_report_name(self) -> str:
        raise NotImplementedError

    def generate_file(self, report_name=None) -> None:
        raise NotImplementedError

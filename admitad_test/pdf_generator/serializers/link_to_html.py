from weasyprint import HTML

from pdf_generator.fields import LinkToHtmlField

from .generic_serializer import GenericSourceToHtmlSerializer


def check_is_ok(data):
    raise Exception


class LinkToHtmlSerializer(GenericSourceToHtmlSerializer):
    def get_fields(self):
        return {
            'html': LinkToHtmlField(write_only=True)
        }

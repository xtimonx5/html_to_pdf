from weasyprint import HTML

from pdf_generator.fields import LinkToHtmlField

from .generic_serializer import GenericSourceToHtmlSerializer


class LinkToHtmlSerializer(GenericSourceToHtmlSerializer):
    def get_fields(self):
        return {
            'html': LinkToHtmlField(write_only=True)
        }

    def create(self, validated_data):
        return validated_data['html']

from django.core.validators import FileExtensionValidator

from pdf_generator.fields import FileToHtmlField
from .generic_serializer import GenericSourceToHtmlSerializer


class FileToHtmlSerializer(GenericSourceToHtmlSerializer):
    def get_fields(self):
        return {
            'html': FileToHtmlField(write_only=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['html', 'htm'])])
        }

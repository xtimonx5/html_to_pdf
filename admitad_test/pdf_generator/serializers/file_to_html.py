from .generic_serializer import GenericSourceToHtmlSerializer
from pdf_generator.fields import FileToHtmlField


class FileToHtmlSerializer(GenericSourceToHtmlSerializer):
    def get_fields(self):
        return {
            'html': FileToHtmlField(write_only=True, )
        }

    def create(self, validated_data):
        return validated_data['html']

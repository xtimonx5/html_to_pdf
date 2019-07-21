import uuid

from django.core.files.base import ContentFile
from weasyprint import HTML
from rest_framework.serializers import CharField, FileField
from django.core.files.storage import default_storage


class LinkToHtmlField(CharField):
    def to_internal_value(self, data):
        return HTML(url=data)


class FileToHtmlField(FileField):
    def to_internal_value(self, data):
        file_name = data.name
        saved_file = default_storage.save(file_name, ContentFile(data.read()))
        return HTML(file_obj=saved_file)

from rest_framework.serializers import FileField, URLField


class LinkToHtmlField(URLField):
    pass


class FileToHtmlField(FileField):
    pass

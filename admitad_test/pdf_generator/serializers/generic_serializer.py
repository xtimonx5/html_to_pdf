from rest_framework.serializers import Serializer


class GenericSourceToHtmlSerializer(Serializer):
    def get_fields(self):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

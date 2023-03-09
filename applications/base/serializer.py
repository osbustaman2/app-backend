from rest_framework import serializers

from applications.base.models import Libro


class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('__all__')
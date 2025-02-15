from rest_framework import serializers
from . import models

class ArmedConflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArmedConflict
        fields = ['title', 'id']

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Files
        fields = ['file', 'title', 'id']

class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medals
        fields = ['image', 'title', 'id']

class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    medals = MedalSerializer(many=True)
    files = FilesSerializer(many=True)
    armed_conflict = ArmedConflictSerializer()

    class Meta:
        model = models.Person
        fields = '__all__'

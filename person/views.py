from . import models, serializers
from rest_framework import generics, response, status

class GetPerson(generics.RetrieveAPIView):
    queryset = models.Person.objects.filter(public=True)
    serializer_class = serializers.PersonSerializer

class CreatePerson(generics.CreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

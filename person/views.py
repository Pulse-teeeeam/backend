from . import models, serializers
from rest_framework import generics, response, status

class GetPerson(generics.RetrieveAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter()
        return self.queryset.filter(public=True)

class CreatePerson(generics.CreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonCreateSerializer

class ArmedConflictsList(generics.ListAPIView):
    queryset = models.ArmedConflict.objects.all()
    serializer_class = serializers.ArmedConflictSerializer

class UpdatePerson(generics.UpdateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonCreateSerializer

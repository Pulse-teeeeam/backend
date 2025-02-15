from . import models, serializers
from rest_framework import generics, response, status
from rest_framework.response import Response


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

from django.db.models import Q

class FindPerson(generics.GenericAPIView):
    serializer_class = serializers.PersonSerializer

    def post(self, request, *args, **kwargs):
        search_params = request.data
        filters = Q()
        for key, value in search_params.items():
            if value:
                filters &= Q(**{key + '__iexact': value})

        queryset = models.Person.objects.filter(filters) if filters else models.Person.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


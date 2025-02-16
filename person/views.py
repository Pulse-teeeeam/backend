from . import models, serializers
from rest_framework import generics, response, status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from .ai import generate


class GetPerson(generics.RetrieveAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.all()
        return self.queryset.filter(public=True)

class CreatePerson(generics.CreateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonCreateSerializer

    def perform_create(self, serializer):
        person = serializer.save()
        models.Logging.objects.create(
            user=self.request.user,
            person=person,
            event='create',
        )

class ArmedConflictsList(generics.ListAPIView):
    queryset = models.ArmedConflict.objects.all()
    serializer_class = serializers.ArmedConflictSerializer

class MedalsList(generics.ListAPIView):
    queryset = models.Medals.objects.all()
    serializer_class = serializers.MedalSerializer

class UpdatePerson(generics.UpdateAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonCreateSerializer

    def perform_update(self, serializer):
        person = serializer.save()
        models.Logging.objects.create(
            user=self.request.user,
            person=person,
            event='edit',
        )

class FindPerson(generics.GenericAPIView):
    serializer_class = serializers.PersonSerializer

    def post(self, request, *args, **kwargs):
        search_params = request.data
        filters = Q()
        for key, value in search_params.items():
            if key == 'armed_conflict':
                filters |= Q(**{key: value})
            elif value:
                filters &= Q(**{key + '__iexact': value})

        if not self.request.user.is_authenticated:
            filters &= Q(public=True)

        queryset = models.Person.objects.filter(filters) if filters else models.Person.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class GenerateAI(APIView):
    def post(self, request, *args, **kwargs):
        person_id = int(kwargs['pk'])
        person = models.Person.objects.get(id=person_id)
        return response.Response({'text': generate(person)})

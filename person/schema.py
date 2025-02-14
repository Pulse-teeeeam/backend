import graphene
from graphene_django.types import DjangoObjectType
from .models import Person, ArmedConflict


class ArmedConflictType(DjangoObjectType):
    class Meta:
        model = ArmedConflict
        fields = "__all__"


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = "__all__"


class CreatePerson(graphene.Mutation):
    class Arguments:
        last_name = graphene.String(required=True)
        first_name = graphene.String(required=True)
        middle_name = graphene.String()
        date_of_birth = graphene.Date(required=True)
        place_of_birth = graphene.String(required=True)
        military_commissariat = graphene.String(required=True)
        military_rank = graphene.String(required=True)
        conflicts_participated = graphene.List(graphene.Int)
        awards = graphene.String(required=True)
        date_of_death = graphene.Date(required=True)
        burial_place = graphene.String(required=True)
        biography_facts = graphene.String()

    person = graphene.Field(PersonType)

    def mutate(self, info, last_name, first_name, middle_name, date_of_birth, place_of_birth, military_commissariat,
               military_rank, conflicts_participated, awards, date_of_death, burial_place, biography_facts):
        person = Person(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            military_commissariat=military_commissariat,
            military_rank=military_rank,
            awards=awards,
            date_of_death=date_of_death,
            burial_place=burial_place,
            biography_facts=biography_facts
        )
        person.save()

        # Add conflicts after saving the person to ensure the object is created first
        person.conflicts_participated.set(conflicts_participated)

        return CreatePerson(person=person)


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()

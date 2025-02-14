import graphene
from account.schema import Query as AuthQuery, Mutation as AuthMutation
from person.schema import Mutation as PersonMutation

class Query(AuthQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, PersonMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

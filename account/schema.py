import graphene
import graphql_jwt
from graphql_jwt.shortcuts import get_token
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model
import uuid  # Добавляем импорт uuid

User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User

class ObtainToken(graphql_jwt.ObtainJSONWebToken):
    user = graphene.Field(UserType)

    def resolve_user(self, info, **kwargs):
        return info.context.user

class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)
    token = graphene.String()

    def mutate(self, info, email, password):
        username = f"{email.split('@')[0]}_{str(uuid.uuid4())[:8]}"
        user = User.objects.create_user(username=username, email=email, password=password)
        
        token = get_token(user)

        return RegisterUser(
            user=user,
            token=token
        )

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, world!")

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    token_auth = ObtainToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

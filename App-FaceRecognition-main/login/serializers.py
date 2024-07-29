from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError, EmailField, CharField, Serializer

from django.contrib.auth import get_user_model
from .models import  UserProfile
from django.contrib.auth.models import Group

User = get_user_model()


class CadastroUsuarioSerializer(serializers.ModelSerializer):
    email_confirma = serializers.EmailField(label='Confirme o email', write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'email_confirma', 'password']
        extra_kwargs = {
            'username': {'validators': []},  # Removendo os validadores padrão do username
        }

    def validate(self, attrs):
        email = attrs.get('email')
        email_confirma = attrs.pop('email_confirma')
        if email != email_confirma:
            raise serializers.ValidationError("Os emails digitados são diferentes")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        email_confirma = validated_data.pop('email_confirma')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

# class CadastroUsuarioSerializer(ModelSerializer):

#     email = EmailField(label='email')
#     email_confirma = EmailField(label='confirme email')

#     class Meta:
#         model = User
#         fields = ['first_name',
#                   'last_name',
#                   'username',
#                   'email',
#                   'email_confirma',
#                   'password']

#     def create(self, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']
#         senha = validated_data['password']
#         email_confirma = validated_data['email_confirma']

#         if User.objects.filter(username=username).exists():
#             raise ValidationError("Informar outro username")

#         if User.objects.filter(email=email).exists():
#             raise ValidationError("Email já associado a um usuário cadastrado")

#         if email != email_confirma:
#             raise ValidationError("Os emails digitados são diferentes")
#         usuario_novo = User(
#             username=username,
#             email=email
#         )
#         usuario_novo.set_password(senha)
#         usuario_novo.first_name = validated_data['first_name']
#         usuario_novo.last_name = validated_data['last_name']
#         usuario_novo.save()
#         return validated_data


class UserListarSerializer(ModelSerializer):

    email = EmailField(label='email')

    class Meta:
        ordering = ['-id']
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'username',
                  'email'
                  ]


class LoginSerializer(ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True, required=True)
    #email = CharField(label='Email Address', allow_blank=True, required=False)

    class Meta:
        model = User
        fields = [

                  'username',
                  'token',
                  'password'

                  ]
        extra_kwards = {'password': {'write_only': True}}

    def validate(self, validated_data):

        username = validated_data.get("username", None)
        senha = validated_data.get("password")

        if not username:
            raise ValidationError("Informe o login para acessar")

        usuario = User.objects.filter(username=username)

        if usuario.exists() and usuario.count() == 1:
            usuario = usuario.first()
        else:
            raise ValidationError("Username incorreto")

        if usuario:
            if not usuario.check_password(senha):
                raise ValidationError("Senha incorreta")

        token, created = Token.objects.get_or_create(user=usuario)

        if not created:
            token.save()

        data = {

            'token':  token.key,
            'username':  validated_data["username"],
            'password':"",
            'id':usuario.id

        }
        return data

class LogoutSerializer(ModelSerializer):
        token = CharField(allow_blank=True, read_only=True)
        username = CharField(allow_blank=True, required=False)
        email = EmailField(label='Email Address', allow_blank=True, required=True)

        class Meta:
            model = User
            fields = ['username',

                      'token'
                      ]

        def logout(self, request):
            try:
               #username = request.get("username")
                #user = User.objects.filter(Q(username=username)).distinct()
                token = Token.objects.get(key= request.get("token"))
                token.delete()

            except (AttributeError, ObjectDoesNotExist):
                pass

            return Response(status=status.HTTP_200_OK)


class UserProfileSerializer(ModelSerializer):


    class Meta:
        model = UserProfile
        fields = ['login',
                  'Cpf',
                  'Nome',
                  'Crm',
                  'Rg',
                  "TipoUsuario"]




from django.core.paginator import Paginator
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import (
    UserListarSerializer,
    LogoutSerializer,
    LoginSerializer,
    CadastroUsuarioSerializer,
    UserProfileSerializer
    )
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import(
    CreateAPIView,
    ListAPIView)
from .models import  UserProfile
from django.shortcuts import render

User = get_user_model()


class UserCreateView (CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CadastroUsuarioSerializer
    queryset = User.objects.all()
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        return render(request, 'usuarios/createUser.html', {'form': serializer})
    
    def post(self, request, *args, **kwargs):

        if(User.objects.filter(username = request.data['username']).exists()):
            return Response('Usuário já cadastrado com o username', status=status.HTTP_400_BAD_REQUEST)
        if (User.objects.filter(email=request.data['email']).exists()):
            return Response('O e-mail informado já foi cadastrado no sistema.', status=status.HTTP_400_BAD_REQUEST)
        serializer = CadastroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Usuário salvo com sucesso", status=HTTP_200_OK)
        return Response("Erro no cadastramento do usuário", status=HTTP_400_BAD_REQUEST)


class UserListViewAll (ListAPIView):

    serializer_class = UserListarSerializer
    queryset = User.objects.all()
    pagination_class = None


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        return render(request, 'usuarios/login.html')
                      
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            return render(request, 'listPrescricoes')
        return render(request, 'usuarios/login.html', {'form': serializer.data})


class LogOutView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LogoutSerializer(data=data)
        if serializer.logout(data):
            return Response("Saiu com sucesso", status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserProfileCreateView (CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def post(self, request, *args, **kwargs):

        print(request.data)
     
        if User.objects.filter(username=request.data['username']).exists():
            return Response("username já cadastrado  favor informar outro username", status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=request.data['email']).exists():
            return Response("email já cadastrado  favor informar outro username", status=HTTP_400_BAD_REQUEST)

        if UserProfile.objects.filter(Cpf=request.data['Cpf']).exists():
            return Response("Cpf já cadastrado  favor informar outro username", status=HTTP_400_BAD_REQUEST)
        login = User.objects.create_user(username=request.data['username'], password=request.data['password'],email=request.data['email'])
        UserProfileData = {
            'login':login.id,
            'Cpf':request.data['Cpf'],
            'Nome':request.data['Nome'],
            'Crm':request.data['Crm'],
            'Rg':request.data['Rg'],
            'TipoUsuario':request.data['TipoUsuario']
        }
        serializer = UserProfileSerializer(data= UserProfileData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Usuário salvo com sucesso", status=HTTP_200_OK)
        return Response("Erro ao cadastrar as informações", status=HTTP_400_BAD_REQUEST)

class UserProfileViewAll (ListAPIView):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    pagination_class = None


def listUsers(request):
    pesquisa = request.GET.get('pesquisa')
    if (pesquisa):
        users = UserProfile.objects.filter(Nome__contains=pesquisa)
    else:
        users = UserProfile.objects.all()
        paginacao = Paginator(users, 10)
        pagina = request.GET.get('page')
        prescricoes = paginacao.get_page(pagina)

    contexto = {'usuarios': users}
    return render(request, 'usuarios/listUsuarios.html', contexto)

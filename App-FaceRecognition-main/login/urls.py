# from os import path
from django.urls import path
from . import views
# from .views import (LoginView,
#                     LogOutView,
#                     UserListViewAll,
#                     UserCreateView,
#                     UserProfileCreateView,
#                     listUsers
#                )

urlpatterns = [
    # path(r'^login/$', LoginView.as_view(), name='login'),
    # url(r'^logout/$', LogOutView.as_view(), name='logout'),
    # url(r'^listar/$', UserListViewAll.as_view(), name='listar'),
    # url(r'^cadastro/$', UserCreateView.as_view(), name='cadastro'),
    # url(r'^userProfile/$', UserProfileCreateView.as_view(), name='cadastro'),
    # path('create/', UserCreateView.as_view(), name='createUser'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('listUsers/', listUsers, name='listUsuarios'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
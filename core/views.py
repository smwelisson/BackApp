from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm


class UsuarioCreate(CreateView):

    # template_name = "account/signup.html"
    form_class = UsuarioForm
    # success_url = reverse_lazy('index')

    # def get_context_data(self):
    #     context = super().get_context_data()
    #
    #     context['titulo'] = 'Registro de novo usuário'
    #     context['botao'] = 'Cadastrar'
    #
    #     return context











# from core.models import User
# from rest_framework import generics
# from core.api.serializers import UserSerializer
#
#
# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

    # permission_classes = [per]

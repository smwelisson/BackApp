from rest_framework import viewsets, permissions
from core.api.serializers import AccountSerializer
from core.models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    # queryset = Account.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        usuario_logado = get_object_or_404(User, pk=self.request.user.id)
        return Account.objects.filter(usuario=usuario_logado)

    def perform_create(self, serializer):
        usuario_logado = get_object_or_404(User, pk=self.request.user.id)
        serializer.save(usuario=usuario_logado)

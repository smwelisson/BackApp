from core.models import User
from rest_framework import generics
from core.api.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [per]

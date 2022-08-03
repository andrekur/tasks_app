from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer

UserModel = get_user_model()


class UserViewCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        UserModel.objects.create_user(**serializer.validated_data)

from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'password', )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'write_only': True, 'required': True}
        }

    def validate_username(self, value):
        if UserModel.objects.filter(username=value).exists():
            return serializers.ValidationError(detail='username must be unique')

        return value

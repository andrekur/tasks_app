from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import TaskModel

UserModel = get_user_model()


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'last_name', 'first_name')
        read_only_fields = fields


class TaskSerializer(serializers.ModelSerializer):
    task_performers = TaskUserSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = TaskModel
        read_only_fields = ('owner', 'create_date')


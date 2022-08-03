from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import TaskModel
from .serializers import TaskSerializer
from .permissions import IsOwner


class MyTaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )

    def get_queryset(self):
        return self.request.user.my_tasks.all()


class UserPerformersTaskViewList(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskModel.objects.filter(task_performers=self.request.user)

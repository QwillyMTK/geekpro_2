from rest_framework import viewsets
from .models import Task
from .serializers import (
    TaskListSerializer,
    TaskDetailSerializer,
    TaskCreateUpdateSerializer
)
class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()

    def get_serializer_class(self):

        if self.action == "list":
            return TaskListSerializer

        if self.action == "retrieve":
            return TaskDetailSerializer

        return TaskCreateUpdateSerializer
from django.db.models import QuerySet
from django_filters import rest_framework as filters


from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Task, SubTask
from .serializers import TaskSerializer, TaskSerializerDetailed, SubTaskSerializer


class TaskFilter(filters.FilterSet):
    name_contains = filters.CharFilter(field_name='name', lookup_expr='icontains')
    description_contains = filters.CharFilter(field_name="description", lookup_expr='icontains')
    minimum_date = filters.DateFilter(field_name='creation_date', lookup_expr='gte', input_formats=['%d-%m-%Y'])
    maximum_date = filters.DateFilter(field_name='creation_date', lookup_expr='lte', input_formats=['%d-%m-%Y'])


class TaskListView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

    @action(detail=True, methods=['post'])
    def end_task(self, request, pk=None) -> Response:
        """
        Given a task id, will close all the subtasks associated with it and set the task status as COMPLETED
        """
        instance = self.get_object()
        subtasks = SubTask.objects.filter(task=instance)
        subtasks_closed = []
        for subtask in subtasks:
            subtask.completed = True
            subtask.save()
            subtasks_closed.append(subtask.id)
        return Response({'closed_subtasks': subtasks_closed})

    @action(detail=False, methods=['get'])
    def detailed_list(self, request) -> Response:
        """
        List all the tasks and subtasks associated with it, as a field called 'subtasks'
        """
        tasks = self.get_queryset()
        serializer = TaskSerializerDetailed(tasks, many=True)
        return Response(serializer.data)

    def filter_by_date_queryset(self, queryset) -> QuerySet:
        date_after = self.request.GET.get('date_after', None)
        date_before = self.request.GET.get('date_before', None)
        if date_after and date_before:
            queryset = queryset.filter(creation_date__range=[date_after, date_before])
        return queryset

    @action(detail=True, methods=['get'])
    def detailed_task(self, request, pk=None) -> Response:
        """
        Given a Task id, list all its field and its subtasks.
        """
        instance = self.get_object()
        if instance:
            serializer = TaskSerializerDetailed(instance)
            return Response(serializer.data)
        return Response("No task found")


class SubTaskModelView(ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        else:
            filters = {'owner': self.request.user}
            task_filter = self.request.query_params.get('task_id')
            if task_filter is not None:
                filters['task_id'] = task_filter
            return self.queryset.filter(**filters)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

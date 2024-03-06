from rest_framework import serializers
from .models import Task, SubTask


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(TaskSerializer, self).to_representation(instance)
        representation['creation_date'] = instance.creation_date.strftime("%d/%m/%Y, %H:%M:%S")
        return representation


class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'

    def _is_user_valid(self, validated_data):
        user = self.context['request'].user
        task_id = validated_data.get('task')
        task_list = Task.objects.get(pk=task_id.id)
        if task_list.owner != user and not user.is_superuser:
            raise serializers.ValidationError("No se encontro la tarea requerida", code='no_permission')

    def create(self, validated_data):
        self._is_user_valid(validated_data)
        return SubTask.objects.create(**validated_data)

    def update(self, instance, validated_data):
        task_id = validated_data.get('task_id')
        if task_id:
            self._is_user_valid(validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TaskSerializerDetailed(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    general_task_status = serializers.ReadOnlyField()
    subtasks_amount = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'subtasks', 'general_task_status', 'subtasks_amount']

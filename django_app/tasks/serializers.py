from rest_framework import serializers

from .models import Todo, PRIORITY


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=256)
    note = serializers.CharField()
    deadline = serializers.DateField(default=None)
    completed = serializers.BooleanField()
    priority = serializers.ChoiceField(choices=PRIORITY, default='2')

    class Meta:
        model = Todo
        fields = ('id', 'title', 'note', 'deadline', 'completed', 'priority')

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.note = validated_data.get('note', instance.note)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.priority = validated_data.get('priority', instance.priority)

from rest_framework import serializers
from .models import Task, Category, Tag
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"
class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "is_completed",
            "created_at",
        )
class TaskDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = "__all__"
class TaskCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
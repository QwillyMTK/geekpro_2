from django.db import models
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    is_completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )

    def __str__(self):
        return self.title
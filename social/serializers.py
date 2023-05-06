from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "content",
            "image",
            "created_at"
        )
        read_only_fields = ("id", "created_at", "author")

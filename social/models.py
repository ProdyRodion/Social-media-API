import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def post_image(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{uuid.uuid4()}{extension}"
    return os.path.join(f"uploads/posts/{slugify(instance.author.email)}",
                        filename)


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to=post_image,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content

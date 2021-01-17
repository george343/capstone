from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    category = models.CharField(max_length=20)
    user_upload = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=100)
    liked = models.ManyToManyField(
        User, related_name="like_user", null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=500)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def serialize(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "video": self.video,
            "commentor": self.commentor
        }

    def __str__(self):
        return self.comment

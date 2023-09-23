from django.db import models
from users.models import User
from events.models import Comment


class Like(models.Model):
    # A simple model that creates a Like Object Instance by adding the User Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="comment_id")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = "likes"

    def __str__(self) -> str:
        return f"Like by User{self.user.id} on Comment {self.comment.id}"

from django.db import models
from users.models import Users
from events.models import Comments

class Likes(models.Model):
    user = models.OneToOneField(Users, models.CASCADE, primary_key=True)  # The composite primary key (user_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.ForeignKey(Comments, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('user', 'comment'),)

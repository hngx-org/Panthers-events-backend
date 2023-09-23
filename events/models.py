from django.db import models
from users.models import Users
import uuid

def generateUUID():
    return str(uuid.uuid4())

class Events(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=generateUUID)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(Users, models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'events'


class Images(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'images'


class Comments(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=generateUUID)
    body = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Events, models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Users, models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'comments'


class CommentImages(models.Model):
    comment = models.OneToOneField(Comments, models.CASCADE, primary_key=True)  # The composite primary key (comment_id, image_id) found, that is not supported. The first column is selected.
    image = models.ForeignKey(Images, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'comment_images'
        unique_together = (('comment', 'image'),)


class EventThumbnail(models.Model):
    image = models.OneToOneField(Images, models.CASCADE, primary_key=True)  # The composite primary key (image_id, event_id) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'event_thumbnail'
        unique_together = (('image', 'event'),)


class InterestedEvents(models.Model):
    event = models.OneToOneField(Events, models.CASCADE, primary_key=True)  # The composite primary key (event_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey(Users, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'interested_events'
        unique_together = (('event', 'user'),)

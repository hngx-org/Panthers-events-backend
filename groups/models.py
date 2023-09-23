from django.db import models
from users.models import User  
from events.models import Event, generateUUID


class Image(models.Model):
    id = models.CharField(max_length=255,
                          primary_key=True,
                          editable=False,
                          default=generateUUID,
                         )
    url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        managed = False
        db_table = 'images'


class Group(models.Model):
    id = models.CharField(max_length=255,
                          primary_key=True,
                          editable=False,
                          default=generateUUID,
                          )
    title = models.CharField(max_length=225)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class meta:
        managed = False
        db_table = 'groups'


class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class GroupEvents(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')

    class Meta:
        managed = False
        db_table = 'group_events'
        unique_together = (('group', 'event'),)


class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='image_id')

    class Meta:
        managed = False
        db_table = 'group_images'
        unique_together = (('group', 'image'),)
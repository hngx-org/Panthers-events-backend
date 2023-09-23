from django.db import models
from users.models import Users
from events.models import Events, Images, generateUUID


class Groups(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=generateUUID)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'groups'

    
class UserGroups(models.Model):
    user = models.OneToOneField(Users, models.CASCADE, primary_key=True)  # The composite primary key (user_id, group_id) found, that is not supported. The first column is selected.
    group = models.ForeignKey(Groups, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class GroupEvents(models.Model):
    group = models.OneToOneField(Groups, models.CASCADE, primary_key=True)  # The composite primary key (group_id, event_id) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_events'
        unique_together = (('group', 'event'),)


class GroupImage(models.Model):
    group = models.OneToOneField(Groups, models.CASCADE, primary_key=True)  # The composite primary key (group_id, image_id) found, that is not supported. The first column is selected.
    image = models.ForeignKey(Images, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_image'
        unique_together = (('group', 'image'),)
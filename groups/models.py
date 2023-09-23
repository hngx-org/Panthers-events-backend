from django.db import models
from users.models import Users
from events.models import Events, Images, generateUUID


class Groups(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=generateUUID)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class meta:
        managed = False
        db_table = 'groups'


class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class GroupEvents(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_events'
        unique_together = (('group', 'event'),)


class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'group_images'
        unique_together = (('group', 'image'),)

from django.db import models
from users.models import User  
from events.models import Event, generateUUID


class Image(models.Model):
    id = models.CharField(max_length=255, primary_key=True, editable=False, default=generateUUID)
    url = models.TextField()

    class meta:
        db_table = 'images'


class Group(models.Model):
    id = models.CharField(max_length=255, primary_key=True, editable=False, default=generateUUID)
    title = models.CharField(max_length=225)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class meta:
        db_table = 'groups'

class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')

    def __str__(self):
        return f"User ID: {self.user}, Group ID: {self.group}"
    
    class Meta:
        db_table = 'user_groups'

class GroupEvents(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')

    def __str__(self):
        return f"Event ID: {self.event}, Group ID: {self.group}"
    
    class Meta:
        db_table = 'group_events'

class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, db_column='image_id')

    def __str__(self):
        return f"Group Name: {self.group.title}, Image URL: {self.image.url}"

    class Meta:
        db_table = 'group_images'
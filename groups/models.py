from django.db import models
from users.models import User
from events.models import Event



class Image(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    url = models.TextField()


class Group(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=225)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"User ID: {self.user_id}, Group ID: {self.group_id}"

class GroupEvents(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Event ID: {self.event_id}, Group ID: {self.group_id}"
    
class GroupImage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"Group Name: {self.group.title}, Image URL: {self.image.url}"
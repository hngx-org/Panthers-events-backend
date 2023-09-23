from django.db import models
from users.models import User
#from groups.models import Image
import uuid

def generateUUID():
    return str(uuid.uuid4())
class Event(models.Model):
    id = models.CharField(max_length=255, primary_key=True, editable=False, default=generateUUID)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    location = models.TextField()
    creator_id = models.ForeignKey(User, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Even_Thumbnail(models.Model):
    #image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)


class Interested_Events(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    id = models.CharField(max_length=255, primary_key=True, editable=False, default=generateUUID)
    body = models.TextField()
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.user_id}'
    
class Comment_Image(models.Model):
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='images')
    image_id = models.ImageField(upload_to='comment_images/')

    def __str__(self) -> str:
        return f"Image for Comment {self.comment_id.id}"

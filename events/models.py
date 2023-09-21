from django.db import models
from users.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    location = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    thumbnail = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.creator}'
    
class Image(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='comment_images/')

    def __str__(self) -> str:
        return f"Image for Comment {self.comment.id}"

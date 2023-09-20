from django.db import models


# Define comment class and other neccesssary fields
class Comment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
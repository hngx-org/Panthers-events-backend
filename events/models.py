from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    start_at = models.DateTimeField() 
    end_at = models.DateTimeField()
    thumbnail = models.CharField(max_length=150)

    def _str_(self):
        return self.title
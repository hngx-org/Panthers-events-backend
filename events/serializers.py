from rest_framework import serializers 
from .models import Comment

class CommentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'timestamp' 'user')

from likes.serializers import LikeSerializer
from likes.models import Like
from events.models import Comment
from rest_framework import generics

"""
    Three Views To :
    - List all Likes
    - List Likes to a particular comment
    - Detail List of 1 Like
"""


class CommentLikes(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        comment_id = self.kwargs['comment_id']
        return self.queryset.filter(comment.id =+ comment_id)
    
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

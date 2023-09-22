from likes.serializers import LikeSerializer
from likes.models import Like
from events.models import Comment, User
from rest_framework import generics, viewsets, status, Response


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
        return self.queryset.filter(comment.id == comment_id)
    
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


# creating a likes on comment
class LikeComment(viewsets.ModelViewset):
    queryset = Like.objects.all()
    serializer = LikeSerializer
    
    def create(self, request, commentId, userId):
        try:
            comment = Comment.objects.get(id=commentId)
            user = User.objects.get(id=userId)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response ({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # check if the user has already liked the comment
        existingLike = Like.objects.filter(comment=comment, user=user).first()
        if existingLike:
            return Response({"message": "User already liked this comment. "}, status=status.HTTP_200_OK)
        
        Like.objects.create(comment=comment, user=user)
        return Response({"message": "Like added to the comment succesfully. "}, status=status.HTTP_201_CREATED)
    
class DeleteLike(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer = LikeSerializer

    def destroy(self, request, commentId, userId):
        try:
            comment = Comment.objects.get(id=commentId)
            user = User.objects.get(id=userId)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has liked the comment
        like = Like.objects.filter(comment=comment, user=user).first()
        if like:
            like.delete()
            return Response({"message": "Like removed from the comment successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "User has not liked this comment."}, status=status.HTTP_200_OK)


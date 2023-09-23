from likes.serializers import LikeSerializer
from likes.models import Likes
from events.models import Comments
from users.models import Users
from rest_framework import generics, viewsets, status, response
from users.authentication import AuthenticationMiddleware,IsAuthenticatedUser


"""
    Three Views To :
    - List all Likes
    - List Likes to a particular comment
    - Detail List of 1 Like
"""


class CommentLikes(generics.ListCreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        comment_id = self.kwargs['comment_id']
        comment = Comments.objects.filter(id=comment_id)
        return self.queryset.filter(comment == comment)
    
class LikeList(generics.ListCreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer

class LikeDetail(generics.ListCreateAPIView):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer


# creating a likes on comment
class LikeComment(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    queryset = Likes.objects.all()
    serializer = LikeSerializer
    
    def create(self, request, commentId, userId):
        try:
            comment = Comments.objects.get(id=commentId)
            user = Users.objects.get(id=userId)
        except Comments.DoesNotExist:
            return response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Users.DoesNotExist:
            return response ({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # check if the user has already liked the comment
        existingLike = Likes.objects.filter(comment=comment, user=user).first()
        if existingLike:
            return response({"message": "User already liked this comment. "}, status=status.HTTP_200_OK)
        
        Likes.objects.create(comment=comment, user=user)
        return response({"message": "Like added to the comment succesfully. "}, status=status.HTTP_201_CREATED)
    
class DeleteLike(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    permission_classes = [IsAuthenticatedUser]
    queryset = Likes.objects.all()
    serializer = LikeSerializer

    def destroy(self, request, commentId, userId):
        try:
            comment = Comments.objects.get(id=commentId)
            user = Users.objects.get(id=userId)
        except Comments.DoesNotExist:
            return response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Users.DoesNotExist:
            return response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has liked the comment
        like = Likes.objects.filter(comment=comment, user=user).first()
        if like:
            like.delete()
            return response({"message": "Like removed from the comment successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response({"message": "User has not liked this comment."}, status=status.HTTP_200_OK)


from rest_framework import viewsets, status, response
from rest_framework.decorators import action

from likes.serializers import LikeSerializer
from likes.models import Likes
from events.models import Comments
from users.models import Users
from users.authentication import AuthenticationMiddleware, IsAuthenticatedUser

class LikeViewSet(viewsets.ModelViewSet):
    authentication_classes = [AuthenticationMiddleware]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    # Create a like for a comment
    @action(detail=False, methods=['post'])
    def create_like(self, request, comment_id, user_id):
        try:
            comment = Comments.objects.get(id=comment_id)
            user = Users.objects.get(id=user_id)
        except Comments.DoesNotExist:
            return response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        except Users.DoesNotExist:
            return response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user has already liked the comment
        existing_like = Likes.objects.filter(comment=comment, user=user).first()
        if existing_like:
            return response({"message": "User already liked this comment."}, status=status.HTTP_200_OK)

        Likes.objects.create(comment=comment, user=user)
        return response({"message": "Like added to the comment successfully."}, status=status.HTTP_201_CREATED)

    # Delete a like for a comment
    @action(detail=False, methods=['delete'])
    def delete_like(self, request, comment_id, user_id):
        try:
            comment = Comments.objects.get(id=comment_id)
            user = Users.objects.get(id=user_id)
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

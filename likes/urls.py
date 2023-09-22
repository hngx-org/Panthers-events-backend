from django.urls import path
from likes.views import CommentLikes, LikeList, LikeDetail
from .views import LikeComment, DeleteLike

"""
    URLs for Listing Likes, Likes in Details and Likes for a comment
"""

urlpatterns = [
    path('likes/', LikeList.as_view(), name='likes'),
    path('likes/<int:comment_id>/', CommentLikes.as_view(), name='comment-likes'),
    path('likes/<int:pk>', LikeDetail.as_view(), name='likes-detail'),
    path('api/comments/<int:commentId>/likes/<int:userId>/', LikeComment.as_view({'post': 'create'}), name='comment-like-create'),
    path('api/comments/<int:commentId>/likes/<int:userId>/', DeleteLike.as_view({'delete': 'destroy'}), name='comment-like-delete')
]

from django.urls import path
from likes.views import CommentLikes, LikeList, LikeDetail

"""
    URLs for Listing Likes, Likes in Details and Likes for a comment
"""

urlpatterns = [
    path('likes/', LikeList.as_view(), name='likes'),
    path('likes/<int:comment_id>/', CommentLikes.as_view(), name='comment-likes'),
    path('likes/<int:pk>', LikeDetail.as_view(), name='likes-detail')
]

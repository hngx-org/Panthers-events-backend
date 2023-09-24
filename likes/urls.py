# from django.urls import path
# from likes.views import CommentLikes, LikeList, LikeDetail
# from .views import LikeComment, DeleteLike

# """
#     URLs for Listing Likes, Likes in Details and Likes for a comment
# """

# urlpatterns = [
#     path("likes/", LikeList.as_view(), name="likes"),
#     path("likes/<str:comment_id>/", CommentLikes.as_view(), name="comment-likes"),
#     path("likes/<str:pk>", LikeDetail.as_view(), name="likes-detail"),
#     path(
#         "api/comments/<str:commentId>/likes/<str:userId>/",
#         LikeComment.as_view({"post": "create"}),
#         name="comment-like-create",
#     ),
#     path(
#         "api/comments/<str:commentId>/likes/<str:userId>/",
#         DeleteLike.as_view({"delete": "destroy"}),
#         name="comment-like-delete",
#     ),
# ]

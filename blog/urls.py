# blog/urls.py
from django.urls import include, path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('blog/post/', BlogModelListView.as_view(), name="post_blog"),
    path('blog/post/<int:id>', BlogModelListView.as_view(), name="post_blog_update"),
    path('blog/post/commment', CommentBoxModelView.as_view(), name="post_comment"),
    path('blog/post/commment/<int:id>', CommentBoxModelView.as_view(), name="post_comment_update"),
    path('chat', ChatView.as_view(), name="chat"),
    path('chat/<int:id>', ChatView.as_view(), name="chat_update"),
    path('blog/like', likeCreateView.as_view(), name="like"),
    path('blog/likeview/<int:id>', LikeDetailsByIDView.as_view(), name="like-view"),
    path('blog/report', reportCreateView.as_view(), name="report"),
    path('blog/reportview', reportByIDView.as_view(), name="report-view"),
    


]
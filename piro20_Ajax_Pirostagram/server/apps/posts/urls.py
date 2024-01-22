from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', main , name='main'),
    path('create/', create, name='create'),
    path('post_like/', post_like, name='post_like'),
    path('comment/', comment, name="comment"),
    path('get_comments/<int:pk>/', get_comments, name="get_comments"),
    path('delete_comment/<int:postId>/<int:commentId>/', delete_comment, name = "delete_comment")
]
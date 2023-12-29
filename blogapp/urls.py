from django.urls import path

from .views import PostsListView, PostDetailView, CommentCreateView

app_name = 'blogapp'

urlpatterns = [
    path('posts/', PostsListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comment/', CommentCreateView.as_view(), name='create_comment'),
]

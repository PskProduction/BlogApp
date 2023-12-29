from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer


class Home(TemplateView):
    template_name = 'index.html'


class PostsListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):

        if self.request.user.is_superuser:
            serializer.save()
        else:
            raise PermissionDenied(detail="Только администратор может создавать посты.")


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    authentication_classes = [TokenAuthentication]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

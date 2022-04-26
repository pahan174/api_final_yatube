from rest_framework import viewsets
from posts.models import Group, Post, Comment, Follow
from .serializers import GroupSerializer, PostSerializer
from .serializers import CommentSerializer, FollowSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins, filters


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny, )


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def destroy(self, request, post_id=None, pk=None):
        comment = get_object_or_404(Comment, id=pk)
        self.check_object_permissions(self.request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateListViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    pass


class FollowViewsSet(CreateListViewSet):
    permissions = (IsAuthenticated, )
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        new_queryset = Follow.objects.filter(user=user)
        return new_queryset

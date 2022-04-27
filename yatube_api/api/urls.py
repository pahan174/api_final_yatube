from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewsSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts_url')
router.register('groups', GroupViewSet, basename='groups_url')
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment_url')
router.register('follow', FollowViewsSet, basename='follow_url')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

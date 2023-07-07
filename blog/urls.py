from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddCommentView,
    LikeView,
)
from . import views

from blog.views import PostLikers
# from users.views import LoginWithGoogle

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('<int:pk>/add_comment/', AddCommentView.as_view(), name = 'add_comment'),
    path('like/<int:pk>/', LikeView, name = 'like_post'),
    path('post_likers/<int:pk>/',PostLikers, name = 'post-likers'),
    # path('accounts/google/login/', LoginWithGoogle, name='GoogleLogin')
]

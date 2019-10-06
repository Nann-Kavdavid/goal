from django.urls import path
from blog_app import views

app_name = 'blog_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('index_new/',),
    path('index/<str:username>/', views.index, name='index-user'),
    path('post/', views.UserPostCreateView.as_view(), name='post'),
    path('comment/<int:pk>/', views.UserCommentCreateView.as_view(), name='comment'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment-approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment-remove'),
    path('users/', views.UserListView.as_view(), name='users'),
]

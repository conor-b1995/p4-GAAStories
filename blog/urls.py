from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('blog_posts/', views.BlogPosts.as_view(), name='blog_posts'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit/<slug:slug>', views.UpdatePost.as_view(), name='update_post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
]

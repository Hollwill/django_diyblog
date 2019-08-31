from django.urls import path
from .views import BlogIndexView, BlogsView, BloggersView, BloggerDetailView, BlogDetailView, CommentCreateView


app_name = 'blog'

urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('bloggers', BloggersView.as_view(), name='bloggers'),
    path('blogger/<int:pk>',
         BloggerDetailView.as_view(), name='blogger_detail'),
    path('<int:pk>/create',
         CommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),

]

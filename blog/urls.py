from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView,BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/yeni', BlogCreateView.as_view(), name='post_yeni'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    
]
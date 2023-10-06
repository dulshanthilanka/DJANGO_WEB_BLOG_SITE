from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name="home_path"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-Update"),
    path('about/', views.about, name="about_path"),
    path('', views.home, name="home_path2"),
]

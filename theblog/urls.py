from django.urls import path

from . views import LikeView, CategoryListView, CategoryView,HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article_details/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('add_post', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('add_category', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:category>/',CategoryView, name='categoryview'),
    path('blog_category/', CategoryListView, name="blog_category"),
    path('like/<int:pk>/', LikeView, name="like_post"),


]

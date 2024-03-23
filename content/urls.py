from django.urls import path
from .views import home, CategoryListView, ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('', home, name='home'),
    path("category/", CategoryListView.as_view(), name="category"),
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("article_detail/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("article_form/", ArticleCreateView.as_view(), name="article_form"),
]

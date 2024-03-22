from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles, Category

def home(request):
    return render(request, 'home.html')

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'content/category.html'

class ArticleListView(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'content/article_list.html'

class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'article'
    template_name = 'content/article_detail.html'


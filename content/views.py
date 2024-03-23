from django.shortcuts import render
from django.views.generic import ListView, DetailView

from content.forms import ArticleForm
from .models import Articles, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticleForm
    template_name = "content/article_form.html"
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
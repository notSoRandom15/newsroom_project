from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

def home(request):
    return render(request, 'home.html')

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'content/category.html'
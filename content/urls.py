from django.urls import path
from .views import home, CategoryListView

urlpatterns = [
    path('', home, name='home'),
    path("category/", CategoryListView.as_view(), name="category"),
]

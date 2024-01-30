from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('blog/', ArticleListView.as_view(), name='blog'),
    path('view/<slug:slug>/', never_cache(ArticleDetailView.as_view()), name='view_article'),
    path('edit/<slug:slug>/', never_cache(ArticleUpdateView.as_view()), name='edit_article'),
    path('delete/<slug:slug>/', never_cache(ArticleDeleteView.as_view()), name='delete_article'),
]

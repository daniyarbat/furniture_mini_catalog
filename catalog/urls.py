from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, categories, contacts, category_items


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/items/', category_items, name='category_items'),
]

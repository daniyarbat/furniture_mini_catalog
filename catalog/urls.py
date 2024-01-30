from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ContactListView, CategoryListView, CategoryCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_list/create/', CategoryCreateView.as_view(), name='create_category'),
    path('products/', ProductListView.as_view(), name='products'),
    path('item/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='item'),
    path('create_item/', never_cache(ProductCreateView.as_view()), name='item_create'),
    path('update_item/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='item_update'),
    path('delete_item/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='item_delete'),
]

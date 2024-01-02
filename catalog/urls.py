from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductList, ContactsView, ProductDetail


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('item/<int:pk>/', ProductDetail.as_view(), name='item')
]

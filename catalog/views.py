from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from catalog.models import Product, Contact


def index(request):
    product_list = Product.objects.all().order_by('pk')
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    context = {
        "page_object": page_object,
        'title': 'Мягкая мебель'
    }
    return render(request, 'catalog/index.html', context)


def show_item(request, product_pk):
    item = get_object_or_404(Product, pk=product_pk)
    context = {
        'item': item,
        'title': item
    }
    return render(request, 'catalog/item.html', context)


class ProductList(ListView):
    paginate_by = 6
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {'title': 'Мягкая мебель'}


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/item.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['item'] = item
        context_data['title'] = item
        return context_data


class ContactsView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты'}
